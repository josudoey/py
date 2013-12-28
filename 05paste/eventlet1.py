#!/usr/bin/env python
import os
from eventlet import wsgi
import eventlet 
from paste.deploy import loadapp  
from paste.deploy import loadserver  
import eventlet
import time 
import eventlet 
from eventlet import greenthread

import logging
import os
log = logging.getLogger(__name__)


from eventlet import event


def background(_pool,*args,**kwargs): 
    while True:
        greenthread.sleep(2) 
        print "greenthread count: %d" % len(_pool.coroutines_running)
    return  


def server_start(_scok,_app_pool,*args,**kwargs):
    eventlet.monkey_patch() 
    wsgi.server( _sock
                ,_app
                ,custom_pool=_pool
                )


if __name__ == '__main__':
    configfile="paste.ini"  
    appname="main"  
    _app = loadapp("config:%s" % os.path.abspath(configfile), appname)  
    _sock=eventlet.listen(('0.0.0.0', 8090))

    _pool = eventlet.GreenPool(1000)  
    _pool.spawn_n(background,_pool) 
    _pool.spawn(server_start,_sock,_app,_pool) 
    ent = event.Event()
    ent.wait()
