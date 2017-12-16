import pandas as pd
import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import numpy as np
import itertools as itool
import datetime
import math
import gc
import os
import struct


rawpath = input("Please enter path where Data is Located \n -> ")
fpath=os.path.normpath(rawpath)
#rawpath = ('C:\\Users\\AWelton\\Documents\\SatFi2\\Alpha\\9_30_16_comparison\\PT43\\usol\\')

outplot = input("Please enter the name you would like for the plot (no file extension) \n -> ")
#outplot = ('testplot_43')

filename = input("Please enter the filename of the top log: ")

header= ['date','time','pid','owner','PR','NI','VIRT','RES','SHR', 'S', 'PERC_CPU','PERC_MEM','TIMEP','COMMAND']

merged_stats = pd.DataFrame()

#using os, join path and input filename for cross platform compatibility
fullpath = os.path.join(fpath,filename)

print(fullpath)

stat = pd.read_csv(fullpath,delim_whitespace=True,names=header)

stat['time'] = stat['time'].map(str).apply(lambda x: x[:-1])


stat['datetime'] = stat['date'].map(str) + ' ' + stat['time'].map(str)

print(stat.head)
stat['datetime'] = pd.to_datetime(stat['datetime'],format="%m\%d\%y %H:%M:%S")


#statistics calculations below
cpu_Q1 = stat['PERC_CPU'].quantile(0.25)
cpu_Q3 = stat['PERC_CPU'].quantile(0.75)
cpu_IQR = cpu_Q3-cpu_Q1

print("\ncpu statistics summary:")
print(stat['PERC_CPU'].describe())
print("\nnasd cpu IQR: " + str(cpu_IQR) )
print("1.5x IQR Filter > " + str(cpu_Q3 + 1.5 * cpu_IQR))

filtered = stat[stat['PERC_CPU'] > (cpu_Q3 + 1.5 * cpu_IQR)]
filtered.to_csv("IQR_filter.csv")

fig, (ax,ax1) = plt.subplots(2,sharex=True)
plt.xticks(rotation=50)

ax.plot_date(stat['datetime'],stat['PERC_CPU'], marker='.',markersize='4', color='dodgerblue')

ax1.plot_date(stat['datetime'],stat['PERC_MEM'],marker='.',markersize='4',color='forestgreen')

ax.xaxis.set_major_formatter(mpl.dates.DateFormatter('%m/%d %H:%M'))
ax.set_title('Top CPU Usage Analysis')
ax.set_ylim(0,100)
ax.set_ylabel('CPU Usage (%)')
ax.legend(loc='upper left')

ax1.xaxis.set_major_formatter(mpl.dates.DateFormatter('%m/%d %H:%M'))
ax1.set_title('Top MEM Usage Analysis')
ax1.set_ylim(0,100)
ax1.set_ylabel('Memory Usage (% of available)')
ax1.legend(loc='upper left')

plt.grid()
plt.draw()
plt.show()
