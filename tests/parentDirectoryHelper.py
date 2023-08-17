import sys, os, inspect

def addParentDirectoryToPath():
    parentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    sys.path.insert(0, parentdir)

def getParentDirectory():
    parentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    return parentdir
