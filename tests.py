import unittest
import tweets
import sys
from subprocess import call
import speech

def halt():
    import pdb; pdb.set_trace()

class EnvironmentTests(unittest.TestCase):

    def testPython3Exists(self):
        version = sys.version_info.major
        self.assertTrue(version >= 3, 'Make sure you run with Python 3!')

    def testMplayerExists(self):
        import os
        with open(os.devnull, 'w') as null:
            out = call(['which', 'mplayer'], stdout=null)
        self.assertEqual(out, 0, 'Mplayer is needed for speech.')


class TwitterTests(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTrue(self):
        self.assertTrue(True)

    def testGetAnythingFromTwitter(self):
        t = tweets.get_tweets(name='allieehenry')
        alstweets = t[1]
        ret_status = t[0]
        self.assertEqual(ret_status, 200)
        self.assertTrue(len(alstweets) >= 1)

    def testNumberRequest(self):
        from tweets import get_tweets
        t = get_tweets(name='JennyJarv', count=7)
        self.assertTrue(len(t[1]) == 7)

    def testNoName(self):
        t = tweets.get_tweets()
        self.assertTrue(t[0] == -1)


class SayTests(unittest.TestCase):

    def testSayIsFound(self):
        from speech import say

    def testRemoveUrls(self):
        s = 'this is a tweet https://twitpic.com/whtever #hash tweet'
        processed = speech.clean(s)
        self.assertEqual(processed, 'this is a tweet #hash tweet')
        s = 'this is a tweet http://twitpic.com/whtever'
        processed = speech.clean(s)
        self.assertEqual(processed, 'this is a tweet ')
        s = 'http://twitpic.com/whtever more #taga'
        processed = speech.clean(s)
        self.assertEqual(processed, 'more #taga')

class SettingsTests(unittest.TestCase):

    def setUp(self):
        with open('testsettings', 'w') as fh:
            print('name = steve', file=fh)
            print('tweets = stevenjarvis|allieehenry', file=fh)
            print('# this is a comment', file=fh)
            print('tweet_no_space=stevenjarvis|allieehenry', file=fh)
            print('tweet_lots_space =  stevenjarvis  | allieehenry', file=fh)
            print('city = marquette,mi', file=fh)

    def tearDown(self):
        import os
        os.remove('testsettings')

    def testGetName(self):
        import settings
        settings.initialize('testsettings')
        self.assertEqual(settings.get_preference('name'), 'steve')

    def testIgnoreComments(self):
        import settings
        settings.initialize('testsettings')
        self.assertEqual(len(settings.prefs), 5)

    def testListPref(self):
        import settings
        settings.initialize('testsettings')
        handles = settings.get_preference('tweets')
        desired = ['stevenjarvis', 'allieehenry']
        self.assertEqual(handles, desired)

    def testLotsOfSpaces(self):
        import settings
        settings.initialize('testsettings')
        handles = settings.get_preference('tweet_lots_space')
        desired = ['stevenjarvis', 'allieehenry']
        self.assertEqual(handles, desired)


if __name__ == '__main__':
    unittest.main()
