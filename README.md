# Clementine_SyncLovedLastfmTracks

This Python 3 script marks loved last.fm tracks of a certain user with 5 stars rating in Clementine music player.
It works also for Strawberry Music Player which is a clone of Clementine.



## Pre-requisites

- Python 3 installed
- Clementine/Strawberry SQLite DB file (e.g. ~/.config/Clementine/clementine.db under Linux)

Note: There's no need to have Clementine/Strawberry installed. The DB file is enough.



## Quickstart

First, ensure that Clementine/Strawberry is not running in order to prevent concurrent access to the SQLite DB file.

If you're using Clementine under Linux you can try the simplest call and hope that the script will find the SQLite DB file at the default path. Just start the Python 3 script and pass the last.fm user as parameter:
```sh
python3 Clementine_SyncLovedLastfmTracks.py LASTFMUSER
```

If this doesn't work or you are under an other OS or using Strawberry you need to add parameter `--pathToDB` to pass the SQLite DB file of Clementine/Strawberry. Example:
```sh
python3 Clementine_SyncLovedLastfmTracks.py LASTFMUSER --pathToDB /path/to/clementine.db
```

Done.

## Where to find Clementine/Strawberry SQLite DB File?

- Clementine: https://groups.google.com/g/clementine-player/c/KJOQmDK9mmI
- Strawberry: https://wiki.strawberrymusicplayer.org/wiki/Accessing_the_database

The path to the DB file needs to be passed by command line parameter `--pathToDB`



## Notes

- In order to avoid data loss ensure that Clementine/Strawberry is not running
- Backup of DB file will be done automatically in same folder

## Compatibility
No issues known so far.

While it should work also under Windows and MacOS in the same way, it was tested only under Linux:
- Strawberry 1.1.1 and Python 3.12.7 under Ubuntu 24.10
- Clementine 1.2 and Python 3.4.0 under Ubuntu Gnome 14.04
- Clementine 1.1.1 and Python 3.3.2 under OpenSUSE 13.1
- Clementine 1.0.1 and Python 3.2.3 under Ubuntu 12.10



## Usage

```
Clementine_SyncLovedLastfmTracks.py LASTFMUSER [options]

This script marks loved last.fm tracks with 5 stars in Clementine.

positional arguments:
  LASTFMUSER            User at last.fm as source for loved tracks

optional arguments:
  -h, --help            show this help message and exit
  --pathToDB CLEMENTINEDB, -d CLEMENTINEDB
                        Full path to Clementine's DB file. Default value:
                        ~/.config/Clementine/clementine.db (which is the
                        default path under Linux)
  --noConfirmation, -n  Suppress confirmation before updating Clementine's DB
                        file.

Backup of Clementine DB will be done automatically.
```

Note: Works for Strawberry music player in the same way as for Clementine.



## Todo

- Auto-detect DB location of Clementine/Strawberry under Windows/MacOS/Linux


## License

MIT
