#coding=utf-8

from User import *

thehttp = '''http://www.pythonchallenge.com/pc/def/channel.html'''
fileaddr = ReplaceWord(thehttp,'html','zip')
if not os.path.isfile('./channel.zip'):
    DownLoadFile(fileaddr,'channel.zip')

import zipfile
zipObj = zipfile.ZipFile('./channel.zip','r')
for file in zipObj.namelist():
    zipObj.extract(file,"channel/")

import re
re_match = re.compile(r'Next nothing is (\d+)(.?$)')
def readNext(FileName):
    FileObj = open(FileName,'r')
    data = FileObj.read()
    FileObj.close()
    nums = re.findall(re_match,data)
    return nums

DocumentPath = './channel/'
FileNow = DocumentPath + '90052.txt'
while 1:
    try:
        #print FileNow
        FileInfo = readNext(FileNow)
        NextNum = FileInfo[0][0]
        try :
            if FileInfo[0][1] != '':
                TxtInfo = FileInfo[0][1]
                print TxtInfo
        except Exception,e:
            TxtInfo = ''
            
        FileNow = DocumentPath + NextNum + '.txt'
        
    except Exception,e:
        print e
        break

FileObj = open(FileNow,'r')
data = FileObj.read()
print data



## used to collect the momments
import zipfile  
zf = zipfile.ZipFile('./channel.zip')  
  
zc = []  
name = '90052.txt'  
while True:  
    f = open('./channel/%s' % name)
    data = f.read().split()[-1]  
    f.close()  
    zc.append(zf.getinfo(name).comment)  
    if data.isdigit():  
        name = '%s.txt' % data  
    else:  
        break  
  
print ''.join(zc)





