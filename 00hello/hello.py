#!/usr/bin/env python
import os,sys
import argparse
import logging
from collections import OrderedDict
from fajoy import config
log = logging.getLogger()

def enable_log(path,logger=log,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'):
    fn=os.path.normpath(os.path.join(os.path.dirname(__file__),path))
    if os.path.isabs(path):
        fn=path
    hdlr = logging.FileHandler(fn)
    hdlr.setFormatter(format)
    log.addHandler(hdlr)
    log.info("enable log in %s "%fn)

def main():
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

    conf=config.defaults()

    if config.has_section("fajoy"):
        conf=OrderedDict(config.items("fajoy"))


    log_fmt="%(asctime)s - [%(threadName)s:%(name)s.%(funcName)s((%(lineno)d))] - %(levelname)s - %(message)s"

    if conf.has_key("log_format"):
        log_fmt=conf["log_format"]

    if args.debug:
        logging.basicConfig(stream=sys.stderr , level=logging.DEBUG, format=log_fmt)

    if args.verbose:
        logging.basicConfig(stream=sys.stderr , level=logging.INFO, format=log_fmt)
    logging.basicConfig(stream=sys.stderr , level=logging.WARNING, format=log_fmt)

    if conf.has_key("log"):
        enable_log(conf["log"])

    if log.isEnabledFor(logging.INFO):
        log.info(conf)

    if log.isEnabledFor(logging.DEBUG):
        log.debug(conf)

    name = args.name or "%s%s" % (conf.get("name"),"(%s)" % conf.get("mail") if conf.has_key("mail") else "")
    msg = " ".join(args.msg) or "hello"

    e = Exception("e")
    log.exception(e)
    print "%s : %s" %(name,msg)

if __name__=="__main__":
    main()
