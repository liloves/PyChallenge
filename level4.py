#coding=utf-8

import re  
re_match = re.compile(r'\D+(\d+$)').match  
  
import sys  
nothing = '63579' 
  
err_num = 0  
pre = ''  
  
import urllib  
for i in xrange(400):  
    try:  
        f = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % nothing)  
        data = f.read()  
        f.close()  
        pre = nothing  
        nums = re_match(data)  
        if nums:  
            nothing = nums.group(1)  
            print i, nothing, data  
        else:  
            print 'no match'  
            break  
    except KeyboardInterrupt:  
        print 'user interrupted'  
        break  
    except Exception, e:  
        err_num += 1  
        print e  
  
print 'previous nothing: %s, error occured: %s times\ndata: %s' % (pre, err_num, data) 
