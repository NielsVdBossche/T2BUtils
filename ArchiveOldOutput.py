#!/usr/bin/env python3

import glob
import re
import os, time, sys
import shutil

from numpy import full

input = "/user/nivanden/ewkino/_FourTopAnalysis/Output/"
target = "/pnfs/iihe/cms/store/user/nivanden/AnalysisOutput/TTTT/"
days = 7
def getTimestamp(filename):
    filenameSplit = filename.split("/")[-1]
    date = ""
    time = ""
    for part in filenameSplit.split('_'):
        if bool(re.match(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", part)):
            date = part
        if bool(re.match(r"[0-9]{2}-[0-9]{2}", part)):
            time = part
            
    return date+"_"+time


if __name__ == "__main__":
    # list all files older than 7 days, take their timestamps and move them to old outputs in a folder named by their timestamp
    now = time.time()
    timestampsChecked = []
    for f in glob.glob(input+"*"):
        timestamp = getTimestamp(f)

        if timestamp in timestampsChecked: continue
        timestampsChecked.append(timestamp)

        if os.stat(f).st_mtime > now - days * 86400: continue
        
        allStampedFiles = glob.glob(input+"*{}*".format(timestamp))

        fullTarget = target + timestamp + "/"
        if not os.path.exists( fullTarget ):
            os.makedirs(fullTarget)
        
        for file in allStampedFiles:
            shutil.move(file, fullTarget)
