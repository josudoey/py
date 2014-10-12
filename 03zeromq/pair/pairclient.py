#!/usr/bin/env python
#ref http://learning-0mq-with-pyzmq.readthedocs.org/en/latest/pyzmq/patterns/pair.html
import zmq
import random
import sys
import time

port = sys.argv[1]
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:%s" % port)

while not socket.closed:
    msg = socket.recv()
    print msg
    socket.send("client message to server1")
    socket.send("client message to server2")
    time.sleep(1)
