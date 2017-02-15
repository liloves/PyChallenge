
import urllib2
import re

theHttp = '''http://www.pythonchallenge.com/pc/def/equality.html'''
context = urllib2.urlopen(theHttp).read()
reptext =  ''.join(re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', context)) 

import webbrowser

nextlevel = theHttp.replace('equality',reptext)
webbrowser.open_new(nextlevel)
