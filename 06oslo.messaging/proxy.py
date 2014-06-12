#!/usr/bin/env python
#ref http://docs.openstack.org/developer/oslo.messaging/server.html
import logging
import contextlib

from oslo.config import cfg
from oslo import messaging
from oslo.messaging._drivers import impl_zmq
from oslo.messaging._executors import impl_eventlet  # FIXME(markmc)


import sys,os
import eventlet
eventlet.monkey_patch()

#logging.basicConfig(level=logging.DEBUG)
CONF=cfg.CONF
CONF.register_opts(impl_zmq.zmq_opts)
CONF.register_opts(impl_eventlet._eventlet_opts)

def parse_args(argv, default_config_files=None):
    CONF(argv[1:],
            project='rpc',
            prog='proxy',
            default_config_files=default_config_files)

def main():
    parse_args(sys.argv,
        default_config_files=(os.path.join(os.path.dirname(__file__),'etc/rpc/server.conf'),)
        )
    with contextlib.closing(impl_zmq.ZmqProxy(CONF)) as reactor:
        reactor.consume_in_thread()
        reactor.wait()

if __name__ == '__main__':
    main()
