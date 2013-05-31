'''
Use the handles in the settings and Twitter api to get the last
tweet of fav peeps.
'''

import json
import urllib.request

def parse(response):
    obj = json.loads(response)
    tweets = [d['text'] for d in obj]
    return tweets

def get_tweets(name=None, count=2):
    # Return tuple of (http status, list of tweets)
    if name == None:
        return (-1, [])
    request_url = ('https://api.twitter.com/1/statuses/user_timeline.json?'
                   'include_entities=true'
                   '&include_rts=true'
                   '&screen_name=%s'
                   '&count=%d' %(name, count))
    with urllib.request.urlopen(request_url) as t:
        status = t.status
        if status == 200:
            result = t.readall().decode('utf-8')
            tweets = parse(result)
            return (t.status, tweets)
    return (status, [])


if __name__ == '__main__':
    pass
