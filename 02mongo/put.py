#!/usr/bin/env python
import os,sys
import argparse
from pymongo import MongoClient
import gridfs

def main():
    parser = argparse.ArgumentParser(description='this is mongo fs example.')
    parser.add_argument('src', metavar='<local path>',type=str, help='store path')
    parser.add_argument('dst', metavar='<mongo filename>',type=str,nargs="?",default=None, help='store path')
    args = parser.parse_args()
    db = MongoClient().gridfs_example
    fs = gridfs.GridFS(db)
    
    if args.dst is None:
        args.dst=os.path.basename(args.src)

    bs = 1024*1024*64
    with open(args.src, "r") as local_file:
        f = fs.new_file(filename=args.dst,chunkSize=bs)
        try:
            while True:
                b = local_file.read(bs)
                if not b:
                    break
                f.write(b)
        finally:
            f.close()
            local_file.close()
        print f._file


if __name__=="__main__":
    main()
