#!/usr/bin/env python
#ref http://learning-0mq-with-pyzmq.readthedocs.org/en/latest/pyzmq/patterns/pair.html
import zmq
import random
import sys
import time

port = sys.argv[1]
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)

while not socket.closed:
    socket.send("Server message to client3")
    msg = socket.recv()
    print msg
    time.sleep(1)
