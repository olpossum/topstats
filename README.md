# topstats
Author: Andy Welton - 7/24/2017

*** REQUIRES PYTHON 3+ ***

These scripts are meant to provide automated analysis of linux top logs.

top_analysis.py takes in specific logs from a process and plots the CPU/MEM usage over time. 
It will also print summary statistics for each process' CPU usage to the console.

In the Stats Summary you will find the following:

count : number of measurements
mean  : mean of the data
std   : standard deviation of the data
min   : minimum value in the data
25%   : value at the 1st quartile
50&   : value at the 2nd quartile
75%   : value at the 3rd quartile
max   : maximum value in the data

IQR   : This prints the computed InterQuartile Range

1.5x IQR Filter : This prints the filter used to identify outliers in the CPU data. Outliers are printed to CSV files in the directory the code was executed from.

generic_top_analysis.py takes in any top log and plots the CPU/MEM usage over time. It will also print the same stats summary.

LOGGING METHOD:

Use the following commands to produce the top logs for analysis:

For top_analysis.py:


For top_analysis_generic.py:

Replace generic with the process name you wish to track

top -b | awk '/generic/ {print system("date -u +\"%m\%d\%y %T\"|tr -d \"\n\""), $0}' >> /var/log/satfi/generic.log &

E.G:
top -b | awk '/java/ {print system("date -u +\"%m\%d\%y %T\"|tr -d \"\n\""), $0}' >> /var/log/satfi/java_top.log &



