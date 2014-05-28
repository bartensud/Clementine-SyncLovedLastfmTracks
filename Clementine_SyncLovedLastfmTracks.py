#!/usr/bin/env python3
# __author__ = 'Thomas Bartensud'

import sqlite3
import sys
import os.path
import shutil
import argparse
from datetime import datetime
from net.elektronengehirn.lastfm import *


scriptDescription = 'This script marks loved last.fm tracks with 5 stars in Clementine.'
parser = argparse.ArgumentParser(description=scriptDescription,
                                 epilog='Backup of Clementine DB will be done automatically.')
parser.add_argument('LASTFMUSER',
                    help='User at last.fm as source for loved tracks',
                    )
parser.add_argument('--pathToDB', '-d',
                    dest='clementineDb',
                    help="Full path to Clementine's DB file. Default value: ~/.config/Clementine/clementine.db (which is the default path under Linux. For an other OS see http://bit.ly/1hiMGNH)",
                    default='~/.config/Clementine/clementine.db',
                    required=False)
parser.add_argument('--noConfirmation', '-n',
                    dest='noConfirmation',
                    action='store_true',
                    help="Suppress confirmation before updating Clementine's DB file.",
                    required=False)
args = parser.parse_args()
#args = parser.parse_args('bartensud -n'.split())
#print(args)
lastfmUser = args.LASTFMUSER
clementineDb = os.path.expanduser(args.clementineDb)
noConfirmation = args.noConfirmation

print(scriptDescription)
print()

print('Get loved tracks for user %s from last.fm...' % lastfmUser)
lfm = LastFM()
tracks = lfm.getLovedTracksByUser(lastfmUser)
print('Found %d loved tracks on last.fm for user %s' %(len(tracks), lastfmUser))
print()


print("Mark loved tracks in Clementine's DB with 5 stars...")
print('Clementine DB File (SQLite): %s' % clementineDb)
if not os.path.isfile(clementineDb):
    print('ERROR - Clementine DB File not found: %s' % clementineDb)
    print("See here to find OS specific location of Clementine's DB file: http://bit.ly/1hiMGNH")
    sys.exit(1)
print('Backup of Clementine DB will be done automatically.')


print('In order to avoid data loss please ensure that Clementine is closed.')
if noConfirmation is False and input('Continue? [y/n] ') != 'y':
    print('Script stopped.')
    sys.exit(1)
print()


print('Creating backup of Clementine DB File %s ...' % clementineDb)
backupDb = '%s_%s.bak' % (clementineDb, datetime.now().strftime('%Y%m%d_%H%M%S'))
if os.path.isfile(backupDb):
    os.remove(backupDb)
if sys.version_info.major >= 3 and sys.version_info.minor >= 3:
    shutil.copy2(clementineDb, backupDb, follow_symlinks=True)
else:
    shutil.copy2(clementineDb, backupDb)
if not os.path.isfile(backupDb):
    print('ERROR - Backup of Clementine DB (%s) to %s failed. Stopping script.' % (clementineDb, backupDb))
    sys.exit(1)
print('Backup finished: %s' % backupDb)
print()


try:
    con = sqlite3.connect(clementineDb)
    cur = con.cursor()


    failedTracks = []
    for track in tracks:
        cur.execute("UPDATE songs SET rating=1 WHERE title=? COLLATE NOCASE AND artist=? COLLATE NOCASE", (track['name'], track['artist']))
        if cur.rowcount > 0:
            print("OK: %s - %s" %(track['artist'], track['name']))
            con.commit()
            #track['updated'] = True
        else:
            print("NOT FOUND: %s - %s" %(track['artist'], track['name']))
            failedTracks.append(track)
            #track['updated'] = False
    print()
    print("Summary: Imported %d of %d loved tracks from last.fm to Clementine (marked with 5 stars)" % (len(tracks)-len(failedTracks), len(tracks)) )
    print("%d tracks could not be found in Clementine DB: %s" % ( len(failedTracks), failedTracks ) )

except sqlite3.Error as e:
    print("ERROR %s:" % e.args[0])
    sys.exit(1)

finally:
    if con:
        con.close()