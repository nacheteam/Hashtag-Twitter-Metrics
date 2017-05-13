import sys
import subprocess
pwd = subprocess.Popen(['/bin/sh','-c','pwd'], stdout=subprocess.PIPE)
path="a"
for line in pwd.stdout:
    if path=="a":
        path=line[:-1]
print(path)
sys.path.append(path+"/src")

import tweepy
import identification

identification.obtainOAuth()
