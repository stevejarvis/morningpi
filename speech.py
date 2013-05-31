'''
Use mplayer to talk.
'''
import re

from subprocess import call

def say(text):
    text = clean(text)
    if len(text) > 100:
        # Apparently translate.google only accepts 100 chars
        text = text[:100]
    call('mplayer -ao alsa -noconsolecontrols\
         "http://translate.google.com/translate_tts?tl=en&q=%s"' %text,
         shell=True)

def clean(text):
    # Remove URLs and apostraphes used in contractions
    text.replace('\'', '')
    return re.sub(r'http:\/\/\S*\s*', '', text)
