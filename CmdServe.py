#coding=utf-8    # 必须用utf8保存中文字符

import os
from Tkinter import *



class Widget():
    def __init__(self):
        
        self.root = Tk()
        #self.root.minsize(400, 200)

        self.btnForm = Frame(self.root)
        
        self.btn1 = Button(self.btnForm,text = "定时关机",command = self.btn1Clicked)
        self.btn2 = Button(self.btnForm,text = "建立wifi",command = self.btn2Clicked)
        self.btn3 = Button(self.btnForm,text = "预留功能",command = self.btn3Clicked)
        self.txt1= Text(self.root)
        
        self.btn1.pack(side = LEFT,anchor = "n")
        self.btn2.pack(side = LEFT,anchor = "n")
        self.btn3.pack(side = LEFT,anchor = "n")
        self.btnForm.pack(side = TOP,anchor = "n")
        
        self.txt1.pack(side = TOP,anchor = "n")
        

        self.shut_mode = 0
    
    def btn1Clicked(self):
        if self.shut_mode == 0:
            Shutdown()
            self.shut_mode = 1
        else:
            Shutdown(0)
            self.shut_mode = 0
            

    def btn2Clicked(self):
        CreatWifiAp('allow')

    def btn3Clicked(self):
        return

    def mainloop(self):
        self.root.mainloop()

    def addMessage(self):
        self.txt1.insert(0.0,text)

'''
    function os.system(cmd) in os module to access the window command line
'''
    
def Shutdown(time = 30):
    if time == 0:
        cmd = 'shutdown -a'         # 取消关机任务
    else:
        cmd = 'shutdown -f -s -t ' + str(time * 60)
    print os.system(cmd)


def CreatWifiAp(mode = 'allow' , ssid = 'VirtualHotPort', key = 82618504):
    if mode == 'disallow':
        cmd = 'netsh wlan set hostednetwork mode=' + mode
        print os.system(cmd)
    elif mode == 'allow':
        cmd = 'netsh wlan set hostednetwork mode=' + mode + ' ssid=' + ssid + ' key='+str(key)
        print os.system(cmd)
        print os.system('netsh wlan start hostednetwork')

if __name__ == "__main__":
    
    winObj = Widget()
    winObj.mainloop()
    
