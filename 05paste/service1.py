#!/usr/bin/env python
import os  
import webob  
from webob import Request  
from webob import Response  

from paste.deploy import loadserver
from paste.deploy import loadapp  
from wsgiref.simple_server import make_server
from pprint import  pformat
import logging
log = logging.getLogger(__name__)

#filter  
class LogFilter():  
    def __init__(self,app):
        self.call_count = 0
        self.app = app  

    def __call__(self,environ,start_response):  
        environ["call_count"] = self.call_count
        self.call_count+=1
        return self.app(environ,start_response)

    @classmethod  
    def factory(cls, global_conf, *args , **kwargs):
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Setup Handler
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(formatter)

        # Setup Logger
        log.addHandler(console)
        log.debug(global_conf)
        log.debug(args)
        log.debug(kwargs)
        return LogFilter

#app
class ShowVersion():  
    def __init__(self,conf,**kwargs):
        self.conf = conf
        self.kwargs = kwargs

    def __call__(self,environ,start_response):
        start_response("200 OK",[("Content-type", "text/plain")])
        context=pformat(self.kwargs,indent=4)   
        return context
    @classmethod  
    def factory(cls,global_conf,**kwargs):
        return ShowVersion(global_conf,**kwargs)

class ShowEnv():  
    def __init__(self):
        pass  
    def __call__(self,environ,start_response,*args,**kwargs):
        req = Request(environ)  
        res = Response()  
        res.status = "200 OK"  
        res.content_type = "text/plain" 
        res.body =  pformat(environ,indent=4)
        return res(environ,start_response)  
    @classmethod  
    def factory(cls,global_conf,**kwargs):  
        logging.basicConfig(filename='showenv.log', level=logging.DEBUG, format="%(asctime)s: %(levelname)s: %(message)s")
        return ShowEnv()

class ShowHead():  
    def __init__(self):
        pass  
    def __call__(self,environ,start_response,*args,**kwargs):
        req = Request(environ)  
        res = Response()
        res.status = "200 OK"  
        res.content_type = "text/plain"  
        res.body =  pformat(req.headers.items(),indent=4)
        return res(environ,start_response)  
    @classmethod  
    def factory(cls,global_conf,**kwargs):  
        return cls()


if __name__ == '__main__':
    configfile="paste.ini"  

    appname="main"  
    wsgi_app = loadapp("config:%s" % os.path.abspath(configfile), appname)  

    servername="main"  
    server = loadserver("config:%s" % os.path.abspath(configfile), servername)
    server(wsgi_app)

    server.serve_forever()  
