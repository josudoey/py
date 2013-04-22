#!/usr/bin/env python
#ref http://docs.python.org/2/library/configparser.html
import ConfigParser
conf = ConfigParser.SafeConfigParser({'DefKey1': 'DefValue1', 'DefKey2': 'DefVaule2'})
conf.read('config')
for s in conf.sections():
    print "[{section}]".format(section=s)
    for op in conf.options(s):
        print "{option} = {value}".format(option=op ,value=conf.get(s,op))
