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
_server=__file__

def parse_args(argv, default_config_files=None):
    CONF(argv[1:],
            project='rpc',
            prog='server',
            default_config_files=default_config_files)

class ServerControlEndpoint(object):

    def __init__(self, server):
        self.server = server

    def stop(self, ctx):
        self.server.stop()

class TestEndpoint(object):
    def test(self, ctxt, arg):
        d ={ "pid":os.getpid(),
              "server":_server , 
               "ctxt" :ctxt , 
               "arg": arg
            }
        print d
        return d

def main():
    parse_args(sys.argv,
        default_config_files=(os.path.join(os.path.dirname(__file__),'etc/rpc/server.conf'),)
        )
    transport = messaging.get_transport(CONF)
    topic="#.%s"%os.getpid()
    target = messaging.Target(
        topic=topic,
        server=_server,
        fanout=False)
    endpoints = [
        ServerControlEndpoint(None),
        TestEndpoint(),
    ]
    print("topic:%s"%topic)
    server = messaging.get_rpc_server(transport, target, endpoints ,executor="eventlet")
    server.start()
    server.wait()

if __name__ == '__main__':
    main()
