from speech import say
from tweets import get_tweets

def read_tweets(user, tweets):
    for tweet in tweets:
        say('%s tweeted %s' %(user, tweet))

def tweets(username, count=2):
    return get_tweets(username, count)[1]


if __name__ == '__main__':
    handles = ['JennyJarv', 'Chris_Lenahen', 'allieehenry', 'stevenjarvis']
    for user in handles:
        t = tweets(user)
        read_tweets(user, t)
