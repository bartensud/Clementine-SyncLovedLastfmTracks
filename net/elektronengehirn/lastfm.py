

__author__="Thomas Bartensud"
__date__ ="$Jul 17, 2010 7:34:02 PM$"

from xml.dom.minidom import parse#, parseString
import urllib.request, urllib.parse, urllib.error


class LastFM:
    """A class for providing a user's loved tracks at last.fm"""
    apiKey = "c0b0c4e03c75ff9c09a87aecf3d7a731" # for last.fm app: LovedSongsImporter 
    trackLimit = 65535
    __url = "http://ws.audioscrobbler.com/2.0/?method=user.getlovedtracks&user=%s&api_key=%s&limit=%d"

    def __init__(self, apiKey=None):
        if apiKey!=None:
            self.apiKey = apiKey


    def getLovedTracksByUser(self, user):
        url = self.__url % (user, self.apiKey, self.trackLimit)
        return self.__getLovedTracksByUrl(url)

    def __getLovedTracksByUrl(self, url):
        print("HTTP GET %s" % (url))
        dom = parse(urllib.request.urlopen(url))
        return self.__getLovedTracksByDOM(dom)

    def __getLovedTracksByDOM(self, dom):
        lovedTracks = []

        # check status
        # ok: <lfm status="ok">
        # failed: <lfm status="failed"><error code="6">Invalid user supplied</error></lfm>
        if 'failed' == dom.firstChild.attributes['status'].value:
            errorEl = dom.getElementsByTagName("error")[0]
            errorCode = errorEl.attributes['code'].value
            errorText = self.__getText(errorEl.childNodes)
            raise LastFMError(errorCode, errorText)

        tracks = dom.getElementsByTagName("track")
        for track in tracks:
            artistEl = track.getElementsByTagName("artist")[0].getElementsByTagName("name")[0]
            artist = self.__getText(artistEl.childNodes) #.encode("utf-8")
            nameEl = track.getElementsByTagName("name")[0]
            name = self.__getText(nameEl.childNodes) #.encode("utf-8")
            lovedTracks.append({'artist':artist, 'name':name})
            #print("%s: %s" % (artist, name))

        print('loved tracks at last.fm: %s' % lovedTracks)
        return lovedTracks

    def __getText(self, nodelist):
        rc = []
        for node in nodelist:
            if node.nodeType == node.TEXT_NODE:
                rc.append(node.data)
        return ''.join(rc)




class LastFMError(Exception):
    def __init__(self, errorCode, errorText):
        self.errorCode = errorCode
        self.errorText = errorText
    def __str__(self):
        return "LastFM Error (%s): %s" % (self.errorCode, self.errorText)



if __name__ == "__main__":
    print("Test")
    lfm = LastFM()

    #url = "lastFM_LovedTracks.xml"
    #url = "lastFM_LovedTracks_reduced.xml"
    #tracks = lfm.getLovedTracks(url)
    tracks = lfm.getLovedTracksByUser('bartensud')
    for track in tracks:
        print(track)
        print(track['artist'])
        print(track['name'])
