#!/usr/bin/env python

import sys

from setuptools import setup

# Think about this later... I'm lazy right now
#   Supporting earlier versions of Python 3 may be simple enough, 
#   but Python 2 may be an ordeal I'm not interested in taking.
if sys.version[:2] < (3, 7):
    raise RuntimeError("EliasFano only supports Python 3.7 or later")

# 


if __name__ == "__main__":
    # Need to do some sanity checking and package version checking
    # Make the setup(...) call after.

