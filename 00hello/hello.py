#!/usr/bin/env python
import os,sys
import argparse
import logging
from collections import OrderedDict
from fajoy import config
log = logging.getLogger()

def enable_log(path):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fn=os.path.normpath(os.path.join(os.path.dirname(__file__),path))
    if os.path.isabs(path):
        fn=path
    hdlr = logging.FileHandler(fn)
    #hdlr.setLevel(logging.DEBUG)
    hdlr.setFormatter(formatter)
    log.addHandler(hdlr)
    log.warning("enable log in %s "%fn)

def enable_verbose():
    log.setLevel(logging.INFO)
    log.info("enable verbose.")

def enable_debug():
    log.setLevel(logging.DEBUG)
    log.debug("enable debug.")

def main():
    logging.basicConfig( stream=sys.stderr , level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    parser = argparse.ArgumentParser(description='this is hello example.')

    parser.add_argument('name', metavar='NAME',type=str, nargs='?',default=None,
                   help='display name.')

    parser.add_argument('msg', metavar='MESSAGE',type=str, nargs='*',
                   help='display a line of text')

    parser.add_argument('-v','--verbose',action='store_true',default=None,
                   help='enable verbose.')

    parser.add_argument('-d','--debug',action='store_true',default=None,
                   help='enable debug.')

    args = parser.parse_args()

    if args.verbose:
        enable_verbose()

    if args.debug:
        enable_debug()

    conf=config.defaults()
    if log.isEnabledFor(logging.DEBUG):
        log.debug(conf)

    if config.has_section("fajoy"):
        conf=OrderedDict(config.items("fajoy"))

    if conf.has_key("log"):
        enable_log(conf["log"])

    if log.isEnabledFor(logging.INFO):
        log.info(conf)

    name = args.name or "%s%s" % (conf.get("name"),"(%s)" % conf.get("mail") if conf.has_key("mail") else "")
    msg = " ".join(args.msg) or "hello"
    print "%s : %s" %(name,msg)

if __name__=="__main__":
    main()
