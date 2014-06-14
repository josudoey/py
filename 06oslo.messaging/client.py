#!/usr/bin/env python
#ref http://docs.openstack.org/developer/oslo.messaging/rpcclient.html
import sys,os
sys.path.insert(0, os.path.join(os.path.dirname(__file__) ))
import logging

import sys,os
from oslo.config import cfg
from oslo import messaging


from hello import rpc
from hello.context import RequestContext
from hello import exception

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

class HelloClient(object):
    def __init__(self, ctxt):
        self.ctxt = ctxt
        self.topic='oslo2.server'
        target = messaging.Target(topic=self.topic,
            version='1.0',
            fanout=False,
            )
        self._client = rpc.get_client( target)

    def stop_all_server(self):
        __client = self._client.prepare(fanout=True)
        return __client.cast(self.ctxt, 'stop')

    def stop_server(self):
        return self._client.cast(self.ctxt, 'stop')
 
    def all_hello(self, arg=None):
        __client =self._client.prepare(fanout=True)
        return __client.cast(self.ctxt, 'hello', arg=arg)

    def hello(self,*args):
        return self._client.call(self.ctxt, 'hello',arg=args )
    
    def hello_kw(self,**kwargs):
        return self._client.call(self.ctxt, 'hello_kw',arg=kwargs)

    def assign_hello(self,server=None,*args):
        __client = self._client.prepare(topic = self.topic)
        if  server:
            __client = self._client.prepare(topic = "%s.%s"%(self.topic,server))
        return __client.call(self.ctxt, 'hello',arg=args )

    def ohno(self,**kwargs):
        return self._client.call(self.ctxt, 'ohno',arg=kwargs)



def main():
    parse_args(sys.argv,
        default_config_files=(os.path.join(os.path.dirname(__file__),'etc/rpc/client.conf'),)
        )
    rpc.init(CONF)
    c=HelloClient(RequestContext("fajoy"))
    ret={}

    print c.all_hello()
    for i in range(3):
        print c.hello("hello",str(i))
        ret = c.hello_kw(a="hello_kw",b="world",c="wow!!!!",i=str(i))
        print ret

    after_server_name = ret.get("server",None)
    for i in range(10):
        print c.assign_hello(after_server_name,"only","you",str(i))
    try:
        c.ohno()
    except exception.HelloException as e:
        print e.message
    #c.stop_server({})
    #.stop_all_server({})

if __name__ == '__main__':
    main()
