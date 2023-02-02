# from guis.guis import *
import os
import traceback
import requests
import urllib3
import sys
from importlib.machinery import SourceFileLoader
version = "1.0.1"
logFile = open("log.txt", "w+")


def patch(self, num_pools=10, headers=None, **connection_pool_kw):
    RequestMethods.__init__(self, headers)
    connection_pool_kw["ca_certs"] = certifi.where()
    self.connection_pool_kw = connection_pool_kw
    self.pools = manager.RecentlyUsedContainer(num_pools, dispose_func=lambda p: p.close())

    # Locally set the pool classes and keys so other PoolManagers can
    # override them.
    self.pool_classes_by_scheme = manager.pool_classes_by_scheme
    self.key_fn_by_scheme = manager.key_fn_by_scheme.copy()


def patchSSL():
    setattr(urllib3.PoolManager, "__init__", patch)


oldInit = getattr(urllib3.PoolManager, "__init__")


def unPatchSSL():
    setattr(urllib3.PoolManager, "__init__", oldInit)


def getPath():
    try:
        from android.permissions import request_permissions, Permission

        request_permissions([Permission.WRITE_EXTERNAL_STORAGE])

        from android.storage import primary_external_storage_path

        primary_ext_storage = primary_external_storage_path()
        """The Android Path"""
        return primary_ext_storage
    except ImportError:
        """The files path"""
        return os.path.dirname(__file__)
    finally:
        print(traceback.format_exc())


def checkSSL():
    try:
        # print('Checking connection to Github...')
        test = requests.get('https://github.com', verify=True)
        # print('Connection to Github OK.')
    except requests.exceptions.SSLError as err:
        print('SSL Error. Adding custom certs to Certifi store...')
    cafile = certifi.where()
    with open('assets/github-com.pem', 'rb') as infile:
        customca = infile.read()
    with open(cafile, 'ab') as outfile:
        outfile.write(customca)
    print('That might have worked.')
    try:
        requests.get('https://github.com')
        return True
    except Exception:
        return False

useDulwich = True

try:
    import git

    useDulwich = False
except git.GitError:
    try:
        from dulwich import porcelain
        import certifi
        from urllib3.request import RequestMethods
        import urllib3.poolmanager as manager
    except Exception:
        print(traceback.format_exc())


file = str(getPath()) + "/RCade"
remoteRepo = 'http://github.com/SuperRedingBros/RKitInstaller.git'


def compatibilityGit(repo, target):
    if useDulwich:
        if not os.path.exists(file):
            gitrepo = git.Repo.clone_from(repo, target)
            gitrepo.close()
        else:
            gitrepo = git.Repo(file)
            try:
                repo.remotes.origin.pull()
            except git.GitError :
                print("Update Failed")
                print("Update Failed: "+traceback.format_exc(), file=logFile)
            gitrepo.close()
    else:
        patchSSL()
        if not os.path.exists(file):
            porcelain.clone(repo, target)
        else:
            porcelain.pull(target, repo)
        unPatchSSL()


# print(script,file=logFile)
sys.path.append(os.path.dirname(sys.executable))
if getattr(sys, 'frozen', False):
    app_path = os.path.dirname(sys.executable)
    sys.path.append(app_path)
else:
    app_path = os.path.dirname(os.path.abspath(__file__))
try:
    SourceFileLoader("Main", file + "/Main.py").load_module()
except Exception as e:
    print(e)
    print(e, file=logFile)
logFile.close()
