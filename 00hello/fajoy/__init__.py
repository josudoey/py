import os,sys
import ConfigParser
import logging
log = logging.getLogger(__name__)
config = ConfigParser.ConfigParser()
config.read(os.path.abspath(os.path.join(__file__,'../../config.ini')))
