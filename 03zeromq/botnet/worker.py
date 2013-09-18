#!/usr/bin/env python
import os
import zmq
import pickle

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://linux1.cs.nctu.edu.tw:17788")

class Task:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def run(self):
        sleep(3)
        return self.a+self.b

if True:
    task=socket.recv_string()
    print task
    #instance=pickle.loads(task)
    #print "begin"
    #result=instance.run()
    result=task+"hello"
    print result
    socket.send_string(result)
