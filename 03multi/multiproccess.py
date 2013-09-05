#!/usr/bin/env python
#ref http://docs.python.org/2/library/multiprocessing.html
from multiprocessing import Pool
from multiprocessing import cpu_count
from time import sleep

def f(x):
    return x*x

pool = Pool(processes=cpu_count())
result=pool.apply_async(f, [1,])
print "get=%s"%result.get(timeout=2)
pool = Pool(processes=cpu_count())
print "map=%s"%pool.map(f, range(10)) 



a=[]
results =[ pool.apply_async(f, [i,],callback=a.append) for i in range(10)]
print "a=%s"%(str(a))
pool.close()
pool.join()
print "a=%s"%(str(a))


pool = Pool(processes=cpu_count())
b=[]
results = pool.map_async(f,range(10),callback=b.append,chunksize=10)

print "b=%s"%(str(b))
results.wait()
print "b=%s"%(str(b))
pool.close()
pool.join()
