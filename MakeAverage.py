#!/usr/bin/python
import csv
import os
import sys

orig_stdout = sys.stdout
csv_f=open('Readings.csv', 'r')
outF = open("myOutFile", "w")
sys.stdout=outF
comm=","
csv_reader = csv.reader(csv_f)
line_count=1
sum=0.0
avg_count=0
for line in csv_reader:
        t=line[1]
        if line_count % 50 != 0:
            sum=sum+float(t)
            line_count=line_count+1
        else:
            avg_count=avg_count+1
            avg=sum/50
            sum=0.0
            line_count=line_count+1
            print(avg_count,avg)



sys.stdout = orig_stdout
outF.close()
csv_f.close()

os.system('cat myOutFile | tr -d \'(\' | tr -d \')\' | tr -d \' \' > avgout.csv')
os.system('rm ./myOutFile')




