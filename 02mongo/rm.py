#!/usr/bin/env python
import os,sys
import argparse
from pymongo import MongoClient
import gridfs
import json
from collections import OrderedDict

def main():
    parser = argparse.ArgumentParser(description='this is mongo fs example.')
    parser.add_argument('regx', metavar='regx',type=str,nargs="?", default=None, help='regex path')
    args = parser.parse_args()
    db = MongoClient().gridfs_example
    fs = gridfs.GridFS(db)
    for l in fs.find({"filename":{"$regex":args.regx}}):
        print "delete %s %s" %(l._id,l._file["filename"])
        fs.delete(l._id)
    


if __name__=="__main__":
    main()
