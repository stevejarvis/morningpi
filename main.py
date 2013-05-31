from speech import say
from tweets import get_tweets

def read_tweets(user, tweets):
    for tweet in tweets:
        say('%s tweeted %s' %(user, tweet))

def tweets(username, count=2):
    return get_tweets(username, count)[1]


if __name__ == '__main__':
    jen_tweets = tweets('JennyJarv', 5)
    al_tweets = tweets('allieehenry', 3)
    read_tweets('Jenny', jen_tweets)
    read_tweets('Allie', al_tweets)
