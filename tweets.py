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
    if name is None:
        return None
    request_url = ('https://api.twitter.com/1/statuses/user_timeline.json?'
                   'include_entities=true'
                   '&include_rts=true'
                   '&screen_name=%s'
                   '&count=%d' %(name, count))
    import pdb; pdb.set_trace()
    with urllib.request.urlopen(request_url) as t:
        status = t.status
        if status == 200:
            result = t.readall().decode('utf-8')
            return parse(result)
        else:
            raise Error('Bad request getting tweets.')


if __name__ == '__main__':
    pass
