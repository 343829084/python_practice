#!/usr/bin/python

##test log
# coding=utf-8  

import logging
import subfile

logging.basicConfig(level=logging.INFO,
                  filename='./log/log.txt',
                  filemode='w',
                  format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
log = logging.getLogger('root.set')
log.setLevel(logging.DEBUG)
if (__name__ == "__main__"):
  log.log(logging.INFO, "main module begin %s","set log level")
  subfile.fun()
  log.debug("main module close %s.","set other msg")