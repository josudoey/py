#!/usr/bin/env python
import sys
class MyConsole:
    """aaaa"""
    def    __init__(self):
        self.mode="main"
        self.funcs=self.get_func("do_"+self.mode)
        self.show_func=getattr(self,"show_"+self.mode)
    def get_func(self,prefix):
        funcs=list()
        for fn in dir(self):
             if fn.startswith(prefix):
                func=getattr(self,fn)
                docs=func.__doc__.split("\n",2)
                funcs.append((docs[0],func))
        return  dict(funcs)

    def show_opts(self):
        for key in self.funcs:
                f=self.funcs[key]
                docs=f.__doc__.split("\n",2)
                cmd=docs[0]
                text=docs[1]
                print "[%s]%s"%(str(key),text)

    def show_main(self):
        print "main function"
        self.show_opts()

    def input_func(self):
        self.show_func()
        sys.stdout.write("input:")
        line=sys.stdin.readline()[:-1]
        if len(line)==0:
                return
        opts=line.split(" ",2)[0]
        funcs=self.funcs
        if funcs.has_key(opts):
                funcs[opts](line)
        else:
                print "[%s] no option"%(opts)


    def main(self):
        while 1:
          self.input_func()


    def do_main_test(self,line):
        """a
        test: testaaa"""
        print "test"
    def do_main_aexit(slef,line):
       """b
(q)    exit"""
       sys,exit(0)


def main():
        c=MyConsole()
        c.main()

if __name__ == "__main__":
    main()

