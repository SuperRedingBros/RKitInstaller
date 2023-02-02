version = "1.0.0"
# from guis.guis import *

import os
import traceback
import requests
import certifi
import urllib3

try:
    print('Checking connection to Github...')
    test = requests.get('https://github.com',verify=True)
    print('Connection to Github OK.')
except requests.exceptions.SSLError as err:
    print('SSL Error. Adding custom certs to Certifi store...')
cafile = certifi.where()
with open('assets/github-com.pem', 'rb') as infile:
    customca = infile.read()
with open(cafile, 'ab') as outfile:
    outfile.write(customca)
print('That might have worked.')

try:
    from android.permissions import request_permissions, Permission

    request_permissions([Permission.WRITE_EXTERNAL_STORAGE])

    from android.storage import primary_external_storage_path

    primary_ext_storage = primary_external_storage_path()
    """url = "https://google.com"
    file = requests.get(url)
    print(file.text)"""


except Exception as e:
    print(e)
    print(traceback.format_exc())

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
import importlib
from importlib.machinery import SourceFileLoader
file = "RCade"
repo = 'http://github.com/SuperRedingBros/RKitInstaller.git'
logFile = open("log.txt", "w+")
import certifi
#print(open(certifi.where()).read())
#os.environ['SSL_CERT_FILE'] = certifi.where()
#ssl.SSLContext.verify_mode = ssl.VerifyMode.CERT_OPTIONAL
"""try:
    import git
    if not os.path.exists(file):
        repo = git.Repo.clone_from(repo, file)
        repo.close()
    else:
        repo = git.Repo(file)
        try:
            repo.remotes.origin.pull()
        except Exception as e:
            print("Update Failed")
            print("Update Failed", file=logFile)
        repo.close()
except:
    pass"""
from dulwich import porcelain
from urllib3.request import RequestMethods
import urllib3.poolmanager as manager
def patch(self, num_pools=10, headers=None, **connection_pool_kw):
    RequestMethods.__init__(self, headers)
    connection_pool_kw["ca_certs"] = certifi.where()
    self.connection_pool_kw = connection_pool_kw
    self.pools = manager.RecentlyUsedContainer(num_pools, dispose_func=lambda p: p.close())

    # Locally set the pool classes and keys so other PoolManagers can
    # override them.
    self.pool_classes_by_scheme = manager.pool_classes_by_scheme
    self.key_fn_by_scheme = manager.key_fn_by_scheme.copy()


setattr(urllib3.PoolManager,"__init__",patch)

if(not os.path.exists(file)):
    porcelain.clone(repo,file)
else:
    porcelain.pull(file,repo)

script = open(file + "/Main.py")
# print(script,file=logFile)
sys.path.append(os.path.dirname(sys.executable))
if getattr(sys, 'frozen', False):
    app_path = os.path.dirname(sys.executable)
    sys.path.append(app_path)
else:
    app_path = os.path.dirname(os.path.abspath(__file__))
SourceFileLoader("Main", file + "/Main.py").load_module()
try:
    pass
except Exception as e:
    print(e)
    print(e, file=logFile)
logFile.close()
