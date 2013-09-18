#!/usr/bin/env python
#ref https://learning-0mq-with-pyzmq.readthedocs.org/en/latest/pyzmq/devices/queue.html
import zmq
import sys
import random


port = "15559"
context = zmq.Context()
print "Connecting to server..."
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:%s" % port)
client_id = random.randrange(1,10005)
#  Do 10 requests, waiting each time for a response

json_dict={
        "worker_id":"",
        "client_id":client_id,
        "a":0,
        "b":0,
        "sum":0
}
 
sum=0
for i in range (1,10):
    json_dict["a"]=i
    json_dict["b"]=json_dict["sum"]
    print "Sending client_id={client_id} a={a} b={b}".format(**json_dict)
    socket.send_json (json_dict)
    #  Get the reply.
    resp = socket.recv_json()
    json_dict.update(resp)
    print "Recving worker_id={worker_id} sum={sum}".format(**resp)

print json_dict
