#!/usr/bin/env python
#ref http://learning-0mq-with-pyzmq.readthedocs.org/en/latest/pyzmq/patterns/pair.html
import zmq
import random
import sys
import time

port = sys.argv[1]
context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.connect("tcp://localhost:%s" % port)

i=0
while not socket.closed:
    msg = socket.recv()
    print msg
