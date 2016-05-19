# /usr/local/bin/python3
# --*-- coding:utf-8 --*--
# __Author__ = 'Jieer'

import multiprocessing
import time
import os

def do_this(what):
    whoami(what)

def whoami(what):
    print('Process %s says: %s' %(os.getpid(),what))

def loopy(name):
    whoami(name)
    start = 1
    stop = 100000
    for num in range(start,stop):
        print("\tNumber %s of %s. Honk!"%(num,stop))
        time.sleep(1)

if __name__ == "__main__":
    whoami("'I'm the main program")
    for n in range(4):
        # p = multiprocessing.Process(target=do_this,args=("I'm functin %s"%n,))
        p = multiprocessing.Process(target=loopy,args=("loopy",))
        p.start()
        time.sleep(1)
        p.terminate()