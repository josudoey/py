#!/usr/bin/env python
#ref http://docs.openstack.org/developer/oslo.messaging/server.html
import logging

from oslo.config import cfg
from oslo import messaging
import sys,os
import eventlet
eventlet.monkey_patch()

#logging.basicConfig(level=logging.DEBUG)
CONF=cfg.CONF

_server=os.getpid()
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
    def hello(self, ctxt,*args,**kwargs):
        d ={   "pid":os.getpid(),
               "server":_server , 
               "ctxt" :ctxt , 
               "args" :args , 
               "kwargs" :kwargs , 
            }
        print d
        return d

    def hello_kw(self, ctxt, *args,**kwargs):
        d ={   "pid":os.getpid(),
               "server":_server , 
               "ctxt" :ctxt , 
               "args" :args , 
               "kwargs" :kwargs , 
            }
        print d
        return d

def main():
    parse_args(sys.argv,
        default_config_files=(os.path.join(os.path.dirname(__file__),'etc/rpc/server.conf'),)
        )
    transport = messaging.get_transport(CONF)
    topic="oslo.server"
    target = messaging.Target(
        topic=topic,
        server=_server,
        )

    ctrl=ServerControlEndpoint()
    endpoints = [
        ctrl,
        TestEndpoint(),
    ]
    print("topic:%s.%s"%(topic,_server))
    server = messaging.get_rpc_server(transport, target, endpoints ,executor="eventlet")
    ctrl.setup(server)
    server.start()
    server.wait()

if __name__ == '__main__':
    main()
