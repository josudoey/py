#!/usr/bin/env python
import zmq
import random
import time

import pickle
from multiprocessing.pool import ThreadPool as Pool
#from multiprocessing import Pool
from time import sleep
import os

context = zmq.Context(io_threads=1)
socket = context.socket(zmq.REQ)
socket.bind("tcp://*:17788")

class Task:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def run(self):
        sleep(3)
        return self.a+self.b


def async(task):
    socket.send_string("1")
    return socket.recv_string()

def callback(result):
    print os.getpid()+":"+result
    
pool = Pool(processes=3)

while True:
    task=Task(1,2)
    t=pickle.dumps(task)
    result=pool.apply_async(async,[t,],callback=callback)
    #pool.apply_async(async,[t,],callback=callback)
    #pool.apply_async(async,[t,],callback=callback)
    #for i in range(3):
    #rep = socket.recv()
