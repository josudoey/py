#!/usr/bin/env python
#ref http://docs.openstack.org/developer/oslo.messaging/rpcclient.html
import logging

import sys,os
from oslo.config import cfg
from oslo import messaging
import eventlet
eventlet.monkey_patch()

#logging.basicConfig(level=logging.DEBUG)
log=logging.getLogger(__name__)
CONF=cfg.CONF
def parse_args(argv, default_config_files=None):
    CONF(argv[1:],
            project='rpc',
            prog='client',
            default_config_files=default_config_files)


class TestClient(object):
    def __init__(self, transport):
        _server=os.getpid()
        self.topic='oslo.server'
        target = messaging.Target(topic=self.topic,
            version='1.0',
            fanout=False,
            )
        self._client = messaging.RPCClient(transport, target)

    def stop_all_server(self, ctxt):
        __client = self._client.prepare(fanout=True)
        return __client.cast(ctxt, 'stop')

    def stop_server(self, ctxt):
        return self._client.cast(ctxt, 'stop')
 
    def all_hello(self, ctxt, arg=None):
        __client =self._client.prepare(fanout=True)
        return __client.cast(ctxt, 'hello', arg=arg)

    def hello(self, ctxt,*args):
        return self._client.call(ctxt, 'hello',arg=args )
    
    def hello_kw(self, ctxt,**kwargs):
        return self._client.call(ctxt, 'hello_kw',arg=kwargs)

    def assign_hello(self, ctxt,server=None,*args):
        __client = self._client.prepare(topic = self.topic)
        if  server:
            __client = self._client.prepare(topic = "oslo.server.%s"%server)
        return __client.call(ctxt, 'hello',arg=args )

def main():
    parse_args(sys.argv,
        default_config_files=(os.path.join(os.path.dirname(__file__),'etc/rpc/client.conf'),)
        )
    ctxt={"ctxt":"hello"}
    transport = messaging.get_transport(CONF)
    c=TestClient(transport)
    ret={}

    print c.all_hello(ctxt)
    for i in range(3):
        ctxt["i"]=i
        print c.hello(ctxt,"hello","world","wow!!!!")
        ret = c.hello_kw(ctxt,a="hello_kw",b="world",c="wow!!!!")
        print ret

    after_server_name = ret.get("server",None)
    for i in range(10):
        ctxt["i"]=i
        print c.assign_hello(ctxt,after_server_name,"only","you",)


    #c.stop_server({})
    #c.stop_all_server({})

if __name__ == '__main__':
    main()
