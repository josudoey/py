#!/bin/bash
cd `dirname $0`
export PYTHONPATH=$PYTHONPATH:`pwd`
paster serve paste.ini
