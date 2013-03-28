#!/usr/bin/env python2
# ref http://zetcode.com/lang/python/functions/
def get_func(obj):
    from inspect import isfunction
    funcs=list()
    for fn in dir(obj):
        func=getattr(obj,fn)
        if isfunction(func):
            funcs.append((fn,func))
    return  dict(funcs)

import sys
class MyConsole:
    """aaaa"""
    def    __init__(self):
        while 1:
            self.run()

    def run(self):
        print sys.stdin.read(1)

def main():
        c=MyConsole()
        c.main()

if __name__ == "__main__":
   main()
   #print __name__
   # print locals()
   # print ch.get_func(locals()["__main__"]).keys()
   # print ch.get_func(ch).keys()
    #main()
