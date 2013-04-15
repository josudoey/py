#!/usr/bin/env python
#ref http://docs.python.org/2/library/argparse.html#module-argparse
import getopt, sys

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
        else:
            assert False, "unhandled option"
    print "verbose = %s"%verbose
    print "output = %s"%output

def usage():
    import os
    prog=os.path.basename(sys.argv[0])
    print "usage: {prog} [-h][-v][-o ouput]".format(prog=prog)

if __name__ == "__main__":
    main()
