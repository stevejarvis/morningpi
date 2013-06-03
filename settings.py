'''
Read settings file for use in the rest of the modules.
'''

def get_preference(key):
    global prefs
    try:
        return prefs[key]
    except KeyError as e:
        print('%s is not set in the settings file.' %key)

def initialize(fname='settings.txt'):
    global prefs
    prefs = {}
    with open(fname, 'r') as fh:
        lines = [l for l in fh.readlines() if l[0] != '#' and l != '\n']
    for line in lines:
        data = line.split('=')
        if '|' in data[1]:
            # Prefs can be used as pipe-separated lists
            value = [v.strip() for v in data[1].split('|')]
        else:
            value = data[1].strip()
        prefs[data[0].strip()] = value

prefs = {}
initialize()
