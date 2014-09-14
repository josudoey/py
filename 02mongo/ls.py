#!/usr/bin/env python
import os,sys
import argparse
from pymongo import MongoClient
import gridfs
import json
from collections import OrderedDict

def main():
    parser = argparse.ArgumentParser(description='this is mongo fs example.')
    args = parser.parse_args()
    db = MongoClient().gridfs_example
    fs = gridfs.GridFS(db)
    for l in fs.list():
        f = fs.get_last_version(l)._file
        print "%s %12s %s %s"% (
                        f["md5"]
                        ,f["length"]
                        ,f["uploadDate"]
                        ,f["filename"]
                        )

if __name__=="__main__":
    main()
