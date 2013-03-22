#!/usr/bin/python2
import os,time,threading

class DetectFileBot(threading.Thread):
    def __init__(self, path):
        threading.Thread.__init__(self)	
	self.path=path
        self.keepGoing = True

    def stop(self):
        self.keepGoing = False
    def getFiles(self,path):
    	if os.path.isfile(path):
	    return (path)
    	if os.path.isdir(path):
	    fs=map(lambda f:path+'/'+f,os.listdir(path))
	    fs=os.listdir(path)

	    fs=filter(os.path.isfile,fs)
	    return fs
	return ()

    def handelFile(self,f):
        s=os.path.getsize(f)
	lines=()
        if s<256:
            fr=open(f, 'r')
	    lines=(l.replace('\n','')  for l in fr.readlines())
	    lines=filter(lambda s:len(s)>0,lines)
            fr.close()
        if s>1: 
            fw = open(f, 'w')
            fw.close()
	if len(lines):
  	    return {f:lines}
	return {}

    def handelFiles(self,fs):
       for f in fs:
           la=self.handelFile(f)
	   def action(k,lines):
	       for l in lines:
	           print l
           for k in la:
               action(k,la[k])

    def run(self):
        while self.keepGoing:
	    fs=self.getFiles(self.path)
	    self.handelFiles(fs)
	    time.sleep(1)


if __name__ == "__main__":
        pwd=os.getenv('PWD')
        f=pwd+'/chanel'
        bot =   DetectFileBot(f)
        bot.start()
        inputStr = ""
        while inputStr != "stop":
            inputStr = raw_input()
        bot.stop()
        bot.join()

