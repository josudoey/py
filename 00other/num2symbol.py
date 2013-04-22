#!/usr/bin/env python

import sys
import re
import math

class u:
    @staticmethod
    def _conv(size):
        if size==0:
            return 0
        t="KMGT"
        s=str(size)
        i=int(math.log(size,2)/10)
        if i==0:
           return s
	if i>4:
	    i=4
        f=float(size)/(2**(i*10))
        r="%.1f"%f
        return r+t[i-1]
    @staticmethod
    def conv(t):
        i=0
        for m in re.finditer(r'(\d+)', t):
            yield t[i:m.start()]
            l=m.end()-m.start()
            d=int(m.group(0))
            w=u._conv(d)
            f="%"+str(l)+"s"
            yield f % (w)
            i=m.end()
        yield t[i:]

for t in u.conv(sys.stdin.read()):
   sys.stdout.write(t)
