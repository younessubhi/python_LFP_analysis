#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 23:08:32 2019

@author: younessubhi
"""

# import libraries
# modules for interacting with OS and accessing functions
import os
import sys

# modules for data analysis and computing
import numpy as np
import pandas as pd
import scipy as sp

# module for signal proc.
import scipy.signal

# modules for data visualisation
import matplotlib.pyplot as plt
import matplotlib.cm
import seaborn as sns

# read/write .mat data
import scipy.io as sio

#### load data

# load mat file(s)
data = sio.loadmat('dorsal_premotor_lfp.mat')

# put keys in variables
lfp = data['lfp']

#### Analysis
## settings

s_rate = 1250 # sampling rate
t_frame = [0,7] # timeframe of data (Seconds)


## plotting
window_len = t_frame[1] - t_frame[0]
# create time array
t_index = np.arange(0,len(lfp)/s_rate,1/s_rate)
# put data in array
t_frame_index = np.where(np.logical_and(t_index>=t_frame[0],t_index<t_frame[1]))[0]

#plot settings
plt.figure(figsize=(12,4))
plt.plot(t_index[t_frame_index],
         lfp[t_frame_index],'b')
sns.set_style('white')
sns.despine()
plt.xticks(size=15); plt.yticks(size=15);
plt.xlabel('time (s)',size=15)
plt.title('t_series of lfp',size=20)
plt.xlim(t_frame)
plt.show()

# Signal proc.: PSD (Power Spectral Density) => PSD shows strength of signal, distributed across freq range
f, psd = sp.signal.welch(lfp[:,0], s_rate, nperseg=1000)

# plot settings
plt.figure(figsize=(11,4))
plt.semilogy(f,psd,'k')
sns.despine()
plt.xlim((0,200))
plt.yticks(size=15)
plt.xticks(size=15)
plt.ylabel('power ($uV^{2}/Hz$)',size=15)
plt.xlabel('freq (Hz)',size=15)
plt.title('psd of lfp', size=20)
plt.show()



