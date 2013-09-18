#!/usr/bin/env python
#ref https://learning-0mq-with-pyzmq.readthedocs.org/en/latest/pyzmq/devices/queue.html
import zmq
def main():

    try:
        context = zmq.Context(1)
        # Socket facing clients
        frontend = context.socket(zmq.REP)
        frontend.bind("tcp://*:15559")
        # Socket facing services
        backend = context.socket(zmq.REQ)
        backend.bind("tcp://*:15560")

        zmq.device(zmq.QUEUE, frontend, backend)
    except Exception, e:
        print e
        print "bringing down zmq device"
    finally:
        pass
        frontend.close()
        backend.close()
        context.term()

if __name__ == "__main__":
    main()
