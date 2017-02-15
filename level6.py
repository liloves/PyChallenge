#coding=utf-8

from User import *

thehttp = '''http://www.pythonchallenge.com/pc/def/channel.html'''
content = OpenUrl(thehttp)
print content

fileaddr = ReplaceWord(thehttp,'html','zip')
DownLoadFile(fileaddr,'channel.zip')


##f=file("channel.txt","w+")
##f.write(content)
##f.close()
