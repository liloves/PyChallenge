#!/usr/bin/env python
#coding=utf-8

import urllib
import urllib2
import os
import re


def OpenUrl(url):
    import webbrowser
    webbrowser.open(url)
    print webbrowser.get()


def Schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print '%.2f%%' % per

def DownLoadFile(HttpAddr,filename = 'defualt.txt'):
    local = os.path.join('./',filename)
    urllib.urlretrieve(HttpAddr,local,Schedule)


def ReadUrl(HttpAddr):
    content = urllib2.urlopen(HttpAddr).read()
    return content

def ReplaceWord(src,undword,repword):
    return src.replace(undword,repword)
