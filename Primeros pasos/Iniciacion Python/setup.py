from distutils.core import setup
import py2exe
import os
import re
import sqlite3
from pathlib import Path
from time import sleep
from random import randrange
import glob

setup(zipfile=None,
      options={'py2exe': {"bundle_files": 1}},
      windows=["3-6-hackerscript.py"])