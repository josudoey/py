#!/usr/bin/env python
import os,sys
def main():
    os.execv("/bin/cat",sys.argv)


if __name__=="__main__":
    main()
