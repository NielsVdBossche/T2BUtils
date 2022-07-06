#!/usr/bin/env python3

import glob
import os, time, sys

days = 7

def deleteOldFiles(path):
    now = time.time()
    for f in glob.glob(path+"*"):
        if os.stat(f).st_mtime < now - days * 86400:
            if os.path.isfile(f):
                os.remove(os.path.join(path, f))


def deleteAllOldCondorfiles():
    subdirs = ["output", "error", "logs"]
    path = "/user/nivanden/condor/"
    for sub in subdirs:
        deleteOldFiles(path+sub+"/")


if __name__ == "__main__":
    deleteAllOldCondorfiles()