#!/usr/bin/env python
import os
import eventlet 
from paste.deploy import loadapp  
from paste.deploy import loadserver  
import eventlet
import time 
import eventlet 
from eventlet import wsgi
from eventlet import greenthread
from eventlet import event
eventlet.monkey_patch() 

import logging
import os
log = logging.getLogger(__name__)



def background(*args,**kwargs): 
    while True:
        greenthread.sleep(2) 
        print "greenthread count: %d" % len(_pool.coroutines_running)
    return  


def server_start(*args,**kwargs):
    wsgi.server( _sock
                ,_app
                ,custom_pool=_pool
                )


if __name__ == '__main__':
    configfile="paste.ini"  
    appname="main"  
    _app = loadapp("config:%s" % os.path.abspath(configfile), appname)  
    _sock=eventlet.listen(('0.0.0.0', 8090))

    _pool = eventlet.GreenPool(100)  
    _pool.spawn_n(background,_pool) 
    _pool.spawn(server_start,_sock,_app,_pool) 
    ent = event.Event()
    ent.wait()
