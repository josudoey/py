#!/usr/bin/env python
#ref https://learning-0mq-with-pyzmq.readthedocs.org/en/latest/pyzmq/devices/queue.html

import zmq
import time
import sys
import random

port = "15560"
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:%s" % port)
worker_id = random.randrange(1,10005)
while True:
    resp = socket.recv_json()
    print "Recving client_id={client_id} a={a} b={b}".format(**resp)
    resp["worker_id"]=worker_id
    resp["sum"]=resp["a"]+resp["b"]
    socket.send_json(resp)
