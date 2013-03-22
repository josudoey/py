#!/usr/bin/ptyhon2
from ircbotframe import ircBot
import sys
import os,time,threading

# Bot specific function definitions
    
def authFailure(recipient, name):
    bot.say(recipient, "You could not be identified")

def quitSuccess(quitMessage):
    bot.disconnect(quitMessage)
    bot.stop()
    
def joinSuccess(channel):
    bot.joinchan(channel)

def saySuccess(channel, message):
    bot.say(channel, message)

def kickSuccess(nick, channel, reason):
    bot.kick(nick, channel, reason)

def identPass():
    pass
    
def identFail():
    pass


def help():
    bot.say(owner, "Join (joins a channel); Usage: \"!join #<channel>\"")
    bot.say(owner, "Kick (kicks a user); Usage: \"!kick <nick> #<channel> <reason>\"")
    bot.say(owner, "Quit (disconnects from the IRC server); Usage: \"!quit [<quit message>]\"")
    bot.say(owner, "Say (makes the bot say something); Usage: \"!say <channel/user> <message>\"")




def privmsg(sender, headers, message):
    if message.startswith("!say "):
        firstSpace = message[5:].find(" ") + 5
        if sender == owner:
            bot.identify(sender, saySuccess, (message[5:firstSpace], message[firstSpace+1:]), authFailure, (headers[0], sender))
    elif message.startswith("!quit"):
        if sender == owner:
            if len(message) > 6:
                bot.identify(sender, quitSuccess, (message[6:],), authFailure, (headers[0], sender))
            else:
                bot.identify(sender, quitSuccess, ("",), authFailure, (headers[0], sender))
    elif message.startswith("!join "):
        if sender == owner:
            bot.identify(sender, joinSuccess, (message[6:],), authFailure, (headers[0], sender))
    elif message.startswith("!kick "):
        firstSpace = message[6:].find(" ") + 6
        secondSpace = message[firstSpace+1:].find(" ") + (firstSpace + 1)
        if sender == owner:
            bot.identify(sender, kickSuccess, (message[6:firstSpace], message[firstSpace+1:secondSpace], message[secondSpace+1:]), authFailure, (headers[0], sender))
    elif message.startswith("!help"):
        help()
    else:
        print "PRIVMSG: \"" + message + "\""
            
def actionmsg(sender, headers, message):
    print "An ACTION message was sent by " + sender + " with the headers " + str(headers) + ". It says: \"" + sender + " " + message + "\""

def endMOTD(sender, headers, message):
    map(bot.joinchan,chanNames)
    df.start()
#    bot.say(chanName, "I am an example bot.")
#    bot.say(chanName, "I have 4 functions, they are Join, Kick, Quit and Say.")
#    bot.say(chanName, "The underlying framework is in no way limited to the above functions.")
#    bot.say(chanName, "This is merely an example of the framework's usage")


	
class DetectFileBot(threading.Thread):
    #{file: action}
    def __init__(self,actions):
        threading.Thread.__init__(self)
	self.actions=actions
#        self.path=path
#	self.action=action
        self.keepGoing = True

    def stop(self):
        self.keepGoing = False
    def getFiles(self,path):
        if os.path.isfile(path):
            return (path)
        if os.path.isdir(path):
            fs=map(lambda f:path+'/'+f,os.listdir(path))
            fs=filter(os.path.isfile,fs)
            return fs
        return ()

    def handelFile(self,f):
        s=os.path.getsize(f)
        lines=()
        if s>1:
	    if s<1024:
                fr=open(f, 'r')
                lines=(l.replace('\n','')  for l in fr.readlines())
                lines=filter(lambda s:len(s)>0,lines)
                fr.close()
            fw = open(f, 'w')
	    fw.flush()
            fw.close()
        if len(lines):
            return {os.path.basename(f):lines}
        return {}

    def handelFiles(self,fs,action):
       for f in fs:
           la=self.handelFile(f)
           def af(k,lines):
               for l in lines:
	           action(k,l)
           for k in la:
               af(k,la[k])

    def run(self):
        while self.keepGoing:
	    for path in self.actions:
                fs=self.getFiles(path)
                self.handelFiles(fs,self.actions[path])
            time.sleep(1)

def chanelsay(chanName,msg):
	bot.say("#"+chanName, msg)
	
def usersay(userName,msg):
	bot.say(userName, msg)

def getChanNames(path):
    if os.path.isdir(path):
        fs=map(lambda f:path+'/'+f,os.listdir(path))
        fs=filter(os.path.isfile,fs)
        fs=map(lambda f:'#'+os.path.basename(f),fs)
        return fs
    return []



# Main program begins here
if __name__ == "__main__":
        server = 'irc.freenode.net'
        port = 6667
        owner = 'fajoy'
	chanDir= os.getenv('PWD')+'/chanel'
	userDir= os.getenv('PWD')+'/user'
        chanNames = getChanNames(chanDir)
	bot = ircBot(server, port, "fajoy_bot", "I am bot of fajoy")
        bot.bind("PRIVMSG", privmsg)
        bot.bind("ACTION", actionmsg)
        bot.bind("376", endMOTD)
        bot.debugging(True)
        bot.start()
	df=DetectFileBot({
	 chanDir:chanelsay,
  	 userDir:usersay,
	})
        inputStr = "" 
        while inputStr != "stop":
            inputStr = raw_input()
        bot.outBuf.sendBuffered("QUIT")  
	df.stop()
        bot.stop()
	df.join()
        bot.join()
