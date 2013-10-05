#!/usr/bin/env python
import subcommand  
from oslo.config import cfg 
from oslo.config.cfg import ConfigOpts
import sys,os
CONF=cfg.CONF
def parse_args(argv, default_config_files=None):
    CONF(argv[1:],
            project='hello',
            prog='world',
            default_config_files=default_config_files)

def main():
    
    parse_args(sys.argv,
        default_config_files=(os.path.join(os.path.dirname(__file__),'etc/hello/world.conf'),)
        )
    CONF = cfg.CONF
    if CONF.verbose:
        print "helloworld"

if __name__ == '__main__':
    main()
