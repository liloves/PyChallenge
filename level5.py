#coding=utf-8

import urllib2

thehttp = '''http://www.pythonchallenge.com/pc/def/banner.p'''
content = urllib2.urlopen(thehttp).read()


import urllib
import os
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


local = os.path.join('./','banner.p')
urllib.urlretrieve(thehttp,local,Schedule)

import pickle
f = open('banner.p')
a = pickle.load(f)

for line in a:  
    print ''.join([x[0] * x[1] for x in line])  
  
f.close()
