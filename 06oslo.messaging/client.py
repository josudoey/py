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
        target = messaging.Target(topic='oslo.server',
            version='1.0',
            fanout=True)
        self._client = messaging.RPCClient(transport, target)
        self._client.prepare(timeout=5)

    def test(self, ctxt, arg):
        return self._client.call(ctxt, 'test22', arg=arg)

def main():
    parse_args(sys.argv,
        default_config_files=(os.path.join(os.path.dirname(__file__),'etc/rpc/client.conf'),)
        )
    ctxt={}
    arg={}
    transport = messaging.get_transport(CONF)
    c=TestClient(transport)
    for i in range(10):
        ctxt["i"]=i
        print c.test(ctxt,arg)

if __name__ == '__main__':
    main()
