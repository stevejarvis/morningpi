from speech import say
from tweets import get_tweets
from weather import get_weather
import settings

def read_tweets(user, tweets):
    for tweet in tweets:
        say('%s tweeted %s' %(user, tweet))

def read_weather():
    # Currently, weather will be a dictionary with a comment, temp, and max.
    location = settings.get_preference('location')
    w = get_weather(location)
    say('The weather for %s includes %s' %(location, w['comment']))
    say('It is currently %d. Expect it to get %.2f degrees warmer'
        %(w['temp'], w['max'] - w['temp']))

def tweets(username, count=2):
    return get_tweets(username, count)[1]


if __name__ == '__main__':
    handles = settings.get_preference('tweets')
    for user in handles:
        t = tweets(user, 1)
        read_tweets(user, t)
    read_weather()
