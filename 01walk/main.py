#!/usr/bin/env python 
import os
walk_path="../"
top_path=os.path.abspath(os.path.join(os.path.dirname(__file__),walk_path ))
start_path=os.path.abspath(os.path.join(os.path.dirname(__file__),walk_path ))
for directory,dirnames,filenames in os.walk(top_path):
    for filename in filenames:
        abspath=directory+"/"+filename
        relpath=os.path.relpath(directory+"/"+filename,start=start_path)
        print (abspath,relpath)
