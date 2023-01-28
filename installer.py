#from guis.guis import *
import pygame
from pygame.locals import *
import random
import pathlib
import math
import pygame
from pygame.locals import *
import json as jsonmod
import random
import glob
import importlib
import sys
import os
import pathlib
import difflib
import zipfile
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg
import numpy
import pylab
import traceback
import inspect
import re
import json
import js2py
from html.parser import HTMLParser
import git
import importlib
from importlib.machinery import SourceFileLoader

file = "RCade"
logFile = open("log.txt","w+")


if(not os.path.exists(file)):
    repo = git.Repo.clone_from('https://github.com/SuperRedingBros/RKitInstaller.git', file)
    repo.close()
else:
    repo = git.Repo(file)
    try:
        repo.remotes.origin.pull()
    except:
        print("Update Failed")
        print("Update Failed",file=logFile)
    repo.close()
script = open(file+"/Main.py")
#print(script,file=logFile)
sys.path.append(os.path.dirname(sys.executable))
if getattr(sys, 'frozen', False):
    app_path = os.path.dirname(sys.executable)
    sys.path.append(app_path)
else:
    app_path = os.path.dirname(os.path.abspath(__file__))
SourceFileLoader("Main",file+"/Main.py").load_module()
try:
    pass
except Exception as e:
    print(e)
    print(e,file=logFile)
logFile.close()
