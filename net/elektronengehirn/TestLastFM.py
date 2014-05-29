import unittest
from net.elektronengehirn.LastFM import *

class  TestLastFM(unittest.TestCase):
    '''
    def setUp(self):
        self.lfm = LastFM()

    def tearDown(self):
        self.lfm.dispose()
        self.lfm = None
    '''
    def testLastFMWithUserBartensud(self):
        lfm = LastFM()
        #lfm = self.lfm
        tracks = lfm.getLovedTracksByUser('bartensud')
        self.assertTrue(tracks is not None)
        #print("Tracks: %s" % tracks)
        self.assertTrue(len(tracks)>0)
        #self.assertTrue(tracks.count>0)
        minExpectedTrack = {'artist': 'Gorillaz', 'name': 'Stylo'}
        minExpectedTrackFound = False
        for track in tracks:
            self.assertTrue(track['artist'] is not None)
            self.assertTrue(track['artist'] != '')
            self.assertTrue(track['name'] is not None)
            self.assertTrue(track['name'] != '')
            if minExpectedTrack['artist']==track['artist'] and minExpectedTrack['name'] == track['name']:
                minExpectedTrackFound = True
        self.assertTrue(minExpectedTrackFound)

    def testLastFMWithTrackLimit1(self):
        trackLimit = 1
        lfm = LastFM()
        lfm.trackLimit = trackLimit
        tracks = lfm.getLovedTracksByUser('bartensud')
        self.assertEqual(trackLimit, lfm.trackLimit)
        self.assertEqual(trackLimit, len(tracks))

'''
    def testLastFMWithNonexistingUser(self):
        nonExistingUser = 'zonUsersa09jf22dsa4a'
        #nonExistingUser = 'bartensud'
        lfm = LastFM()
        #self.assertr.assertRaises(LastFMError, lfm.getLovedTracksByUser,'zonUsersa09jf22dsa4a')
        try:
            lfm.getLovedTracksByUser(nonExistingUser) # todo: handle HTTP Error 400 (Bad request)
            self.fail("This test passed although an exception was expected: 'invalid user supplied' (user: '%s')" %(nonExistingUser))
        except LastFMError as e:
            if e.errorCode != "6":
                raise

    def testLastFMWithInvalidApikey(self):
        lfm = LastFM()
        lfm.apiKey = "invalidKey"
        try:
            lfm.getLovedTracksByUser('bartensud') # todo: handle HTTP Error 403 (Forbidden)
            self.fail("This test passed although an exception was expected: 'Invalid API key' (api key used: '%s')" %(lfm.apiKey))
        except LastFMError as e:
            if e.errorCode != "10":
                raise

'''

if __name__ == '__main__':
    unittest.main()

