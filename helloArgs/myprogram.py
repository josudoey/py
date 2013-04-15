#!/usr/bin/env python
#ref http://docs.python.org/2/library/argparse.html#module-argparse
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--foo', help='foo help')
args = parser.parse_args()
