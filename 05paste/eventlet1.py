#!/usr/bin/env python
import os
import eventlet 
from eventlet import wsgi
from eventlet import event
from paste.deploy import loadapp  
import time 
eventlet.monkey_patch() 

def background(pool,*args,**kwargs): 
    while True:
        time.sleep(2) 
        print "greenthread count: %d" % len(pool.coroutines_running)
    return  

def server_start(sock,app,pool):
    wsgi.server( sock ,app ,custom_pool=pool )

if __name__ == '__main__':
    configfile="paste.ini"  
    appname="main"  
    _app = loadapp("config:%s" % os.path.abspath(configfile), appname)  
    _sock=eventlet.listen(('0.0.0.0', 8090))

    _pool = eventlet.GreenPool(100)  
    _pool.spawn_n(background,_pool) 
    _pool.spawn_n(server_start,_sock,_app,_pool) 
    ent = event.Event()
    ent.wait()
