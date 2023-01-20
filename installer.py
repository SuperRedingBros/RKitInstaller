import os
import sys
import git

file = "RCade"

if(not os.path.exists(file)):
    repo = git.Repo.clone_from('https://github.com/SuperRedingBros/RKitInstaller.git', file)
else:
    repo = git.Repo(file)
    repo.remotes.origin.pull()
    repo.close()
script = open(file+"/Main.py")
exec(script.read())

quit()
