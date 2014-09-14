#!/usr/bin/env python
import os,sys
import argparse
from pymongo import MongoClient
import gridfs
import json
from collections import OrderedDict

def main():
    parser = argparse.ArgumentParser(description='this is mongo fs example.')
    parser.add_argument('regx', metavar='regx',type=str,nargs="?", default="", help='regex path')
    args = parser.parse_args()
    db = MongoClient().gridfs_example
    fs = gridfs.GridFS(db)
    for l in fs.find({"filename":{"$regex":args.regx}}):
        print l.__dict__


if __name__=="__main__":
    main()
