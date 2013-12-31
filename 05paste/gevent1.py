#!/usr/bin/env python

import os
from paste.deploy import loadapp
import gevent
import random
from gevent import pywsgi
from gevent.pool import Pool
from geventwebsocket.handler import WebSocketHandler
from HTMLParser import HTMLParser

participants = set()

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    ">": "&gt;",
    "<": "&lt;",
    }

def escape(text):
    return "".join(html_escape_table.get(c,c) for c in text)

def background(_pool,*args,**kwargs):
    from  pprint import pformat
    while True:
        gevent.sleep(2)
        print "participants count: %d" % len(participants)
    return

def websocket_chat_app(environ, start_response):
    from datetime import datetime
    ws = environ["wsgi.websocket"]
    message = ws.receive()
    rip = environ["REMOTE_ADDR"]
    participants.add(ws)

    t = datetime.now().strftime('%H:%M:%S')
    m = "(%s %s add room.)" % (rip,t)
    for p in participants:
            p.send(m)
    try:
        while True:
            t = datetime.now().strftime('%H:%M:%S')
            m ="%s[%s]: %s" % (rip,t,escape(ws.receive()))
            if m is None:
                break
            for p in participants:
                p.send(m)
    finally:
        participants.remove(ws)

def plot_graph_app(environ, start_response):
    ws = environ["wsgi.websocket"]
    message = ws.receive()
    ws.send(message)
    for i in xrange(100):
        ws.send("0 %s %s\n" % (i, random.random()))
        gevent.sleep(0.1)
    ws.close()
    
if __name__ == "__main__":
    configfile="paste.ini"
    appname="main"
    wsgi_app = loadapp("config:%s" % os.path.abspath(configfile), appname)
    wsgi_app['/data']=plot_graph_app
    wsgi_app['/chat']=websocket_chat_app

    _pool = Pool(100)
    _pool.spawn(background,_pool)
    server = pywsgi.WSGIServer(("0.0.0.0", 8100)
                ,wsgi_app
                ,handler_class=WebSocketHandler)

    server.serve_forever()

