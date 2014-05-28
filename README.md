Clementine_SyncLovedLastfmTracks
================================

This Python 3 script marks loved last.fm tracks with 5 stars rating in Clementine audio player.

by Thomas Bartensud


PRE-REQUISITES:
--------------
- Python 3 installed
- Clementine SQLite DB File, see http://bit.ly/1hiMGNH (while Clementine itself is not needed)

Tested with
- Clementine 1.0 and Python 3.2 under Ubuntu 12.10
- Clementine 1.2 and Python 3.4 under Ubuntu Gnome 14.04

QUICKSTART
--------------
If you're under Linux, just start the Python 3 script and pass the last.fm user:
python3 Clementine_SyncLovedLastfmTracks.py LASTFMUSER

For an other OS you need to pass also the Clementine's DB file (see parameter --pathoDB below)

USAGE:
--------------
Clementine_SyncLovedLastfmTracks.py [-h] [--pathtoDB CLEMENTINEDB]
                                           [--noConfirmation]
                                           LASTFMUSER

This script marks loved last.fm tracks with 5 stars in Clementine.

positional arguments:
  LASTFMUSER            User at last.fm as source for loved tracks

optional arguments:
  -h, --help            show this help message and exit
  --pathtoDB CLEMENTINEDB, -d CLEMENTINEDB
                        Full path to Clementine's DB file. Default value:
                        ~/.config/Clementine/clementine.db (which is the
                        default path under Linux. For an other OS see
                        http://bit.ly/1hiMGNH)
  --noConfirmation, -n  Suppress confirmation before updating Clementine's DB
                        file.

NOTES:
--------------
- In order to avoid data loss ensure that no Clementine process is running
- Backup of Clementine DB (SQLite file) will be done automatically


TODO:
--------------


LICENSE
--------------
tbd