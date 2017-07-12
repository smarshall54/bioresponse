#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 16:30:47 2017

@author: steve
"""
import matplotlib.pyplot as plt
import numpy as np

prilepin_low = {}
prilepin_opt = {}
prilepin_hi = {}

prilepin_low = {55:30,70:24,80:20,90:10}
prilepin_opt = {60:24, 75:18, 85:15, 92.5:4}
prilepin_hi = {65:18,80:12,90:10, 95:2}

prilepin_range = [prilepin_low, prilepin_opt, prilepin_hi]



fig1 = plt.figure()
ax1 = fig1.add_subplot(212)
ax2 = fig1.add_subplot(211)

for ele in prilepin_range:
    intensity = []
    reps = []
    volume = []
    for key in ele:
        intensity.append(key)
        reps.append(ele[key])
        volume.append((key/100)*ele[key])
    ax1.plot(intensity,reps)
    ax2.plot(intensity,volume)

ax1.set_ylabel('reps')
ax1.set_xlabel('intensity')
ax2.set_ylabel('volume')
ax1.legend(loc=2)
#plt.show()


####
# 5/3/1 Program
####

#   65x5   70x3   75x5
#   75x5   80x3   85x3
#   85x5   90x3   95x1


week1 = {65:5,75:5,85:5}
week2 = {70:3, 80:3, 90:3}
week3 = {75:5, 85:3, 95:1}
five31 = [week1, week2, week3] 

fig2 = plt.figure()
ax1 = fig2.add_subplot(212)
ax2 = fig2.add_subplot(211)

for ele in five31:
    intensity = []
    reps = []
    volume = []
    for key in ele:
        intensity.append(key*.9)
        reps.append(ele[key])
        volume.append((key*.9/100)*ele[key])
        # really want to add the volume from all 3 weeks together and plot that
        # to compare to prilepin
    ax1.plot(intensity,reps)
    ax2.plot(intensity,volume)
    
ax1.set_ylabel('reps')
ax1.set_xlabel('intensity')
ax2.set_ylabel('volume')