#coding=utf-8

import urllib2

thehttp = '''http://www.pythonchallenge.com/pc/def/ocr.html'''
content = urllib2.urlopen(thehttp).read()

a_end = content.find(r'-->') + len(r'-->')
d_start = content.find(r'<!--',a_end) + len(r'<!--')
d_stop  = content.find(r'-->',a_end)
kData = content[d_start:d_stop]

a = ''
for i in kData:
    if i.isalpha():
        a = a+i

print a

import webbrowser
nextlevel = thehttp.replace('ocr',a)
webbrowser.open_new(nextlevel)


