#!/usr/bin/env python
#ref http://learning-0mq-with-pyzmq.readthedocs.org/en/latest/pyzmq/patterns/pair.html
import zmq
import random
import sys
import time

port = sys.argv[1]
context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://*:%s" % port)

i=0
while not socket.closed:
    print "push %s" %i
    socket.send("%s: push Server message to client"%i)
    time.sleep(1)
    i+=1
