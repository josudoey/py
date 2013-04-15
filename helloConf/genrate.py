#!/usr/bin/env python
#ref http://docs.python.org/2/library/configparser.html
import ConfigParser
conf = ConfigParser.SafeConfigParser({'name':'fajoy','email' : 'wuminfajoy@gmail.com'})
conf.add_section('helloSection')
conf.set('helloSection','git', 'https://github.com/')
conf.add_section('helloSection2')
conf.set('helloSection2','git', 'https://github.com/fajoy/')

with open('config', 'wb') as configfile:
    conf.write(configfile)
