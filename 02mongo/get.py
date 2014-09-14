#!/usr/bin/env python
import os,sys
import argparse
from pymongo import MongoClient
import gridfs

def main():
    parser = argparse.ArgumentParser(description='this is mongo fs example.')
    parser.add_argument('src', metavar='<mongo filename>',type=str, help='store path')
    parser.add_argument('dst', metavar='<local path>',type=str,nargs="?",default=None,  help='store path')
    args = parser.parse_args()
    db = MongoClient().gridfs_example
    fs = gridfs.GridFS(db)
    if args.dst is None:
        args.dst=os.path.basename(args.src)
    o = fs.get_last_version(args.src)
    with open(args.dst, "w") as f:
        try:
            while True:
                b = o.read(o.chunkSize)
                if not b:
                    break
                f.write(b)
        finally:
            o.close()
            f.close()

if __name__=="__main__":
    main()
