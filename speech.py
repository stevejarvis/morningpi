'''
Use mplayer to talk.
'''

from subprocess import call

def say(text):
    call('mplayer -ao alsa -noconsolecontrols\
         "http://translate.google.com/translate_tts?tl=en&q=%s"' %text,
         shell=True)
