#!/usr/bin/env python
#ref http://docs.openstack.org/developer/oslo.messaging/server.html
import sys,os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

import logging

from oslo.config import cfg
from oslo import messaging
import sys,os
import eventlet

from hello import rpc
from hello import exception
eventlet.monkey_patch()

#logging.basicConfig(level=logging.DEBUG)
CONF=cfg.CONF

def parse_args(argv, default_config_files=None):
    CONF(argv[1:],
            project='rpc',
            prog='server',
            default_config_files=default_config_files)

class ServerControlEndpoint(object):

    def __init__(self):
        pass

    def setup(self, server):
        self.server = server

    def stop(self, ctx):
        self.server.stop()

class TestEndpoint(object):
    def __init__(self,server_name):
        self.server_name=server_name
        
    def hello(self, ctxt,*args,**kwargs):
        d ={   "pid":os.getpid(),
               "server":self.server_name , 
               "args" :args , 
               "kwargs" :kwargs , 
            }
        print d
        return d

    def hello_kw(self, ctxt, *args,**kwargs):
        d ={   "pid":os.getpid(),
               "server":self.server_name , 
               "args" :args , 
               "kwargs" :kwargs , 
            }
        print d
        return d

    def ohno(self, ctxt, *args,**kwargs):
        raise exception.HelloException("oops")

def main():
    parse_args(sys.argv,
        default_config_files=(os.path.join(os.path.dirname(__file__),'etc/rpc/server.conf'),)
    )
    rpc.init(CONF)
    topic="oslo2.server"
    server_name = os.getpid()

    target = messaging.Target(
        topic=topic,
        server=server_name,
    )

    ctrl=ServerControlEndpoint()
    endpoints = [
        ctrl,
        TestEndpoint(server_name),
    ]

    print("topic:%s.%s"%(topic,server_name))
    server = rpc.get_server( target, endpoints)
    ctrl.setup(server)
    server.start()
    server.wait()

if __name__ == '__main__':
    main()
