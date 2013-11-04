#!/usr/bin/env python
import os
import time
import signal
import logging

logging.basicConfig(filename='hup.log', level=logging.INFO,
    format="%(asctime)s: %(levelname)s: %(message)s")
log = logging.getLogger(__name__)


running = True

def run():
    log.info('PROGRAM STARTUP')
    log.info('Current pid: %d' % os.getpid())

    while running:
        log.info('Doing some hard work')
        time.sleep(10)
    else:
        log.info('PROGRAM TEARDOWN')

def signal_handler(signum, frame):
    log.info("Received Signal: %s at frame: %s" % (signum, frame))

    if signum == signal.SIGTERM:
        log.info('Received request to terminate daemon (SIGTERM)')
        global running
        running = False
    elif signum == signal.SIGHUP:
        #"kill -HUP <pid>"
        #"kill -s 1 <pid>"
        log.info('Received reload config request (SIGHUP)')
        pass  # reload config here


def main():
    # Produce formater first
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
 
    # Setup Handler
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
 
    # Setup Logger
    log.addHandler(console)
    log.setLevel(logging.DEBUG)

    signal.signal(signal.SIGHUP, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    run()
 
if __name__ == '__main__':
    main()

    
