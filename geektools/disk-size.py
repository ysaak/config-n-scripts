#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, math
import set_progress

def convertSize(bytes):
    if bytes < 1024:
        return str(round(bytes,2)) + ' Kio'
    elif bytes < 1048576:
        return str(round(bytes / 1024,2)) + ' Mio'
    else:
        return str(round(bytes / 1048576,2)) + ' Gio'

def buildProgressBar(percent):
    # colors
    red = "\033[31m"
    yellow = "\033[33m"
    green = "\033[32m"
    clear = "\033[0m"

    meter = ""

    for i in range(1, 11):
        if percent >= 10:
            if i <= 2: # first 2 bars red
                meter += red
            elif i <= 5: # next 3 bars yellow
                meter += yellow
            else: # remaining 5 green
                meter += green
            meter += "❚" + clear # clear color
        else:
            meter += "." + clear

        percent -= 10 # decrement percentage for next loop

    return meter

s = os.statvfs('/')

free = float(s.f_bavail * s.f_frsize) / 1024
percent = float(s.f_bavail) / float(s.f_blocks) * 100


print "\033[1mHDD\033[0m\n", convertSize(free)

set_progress.setProgressImage("disk-progress", percent)
