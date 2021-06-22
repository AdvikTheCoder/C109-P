import pandas as pd
import statistics 
import csv

df=pd.read_csv('SD.csv')
height=df['Height(Inches)'].tolist()
mean=statistics.mean(height)
mode=statistics.mode(height)
median=statistics.median(height)
sd=statistics.stdev(height)
start1,end1,start2,end2,start3,end3=mean-sd,mean+sd,mean-2*sd,mean+2*sd,mean-3*sd,mean+3*sd

data1=[result for result in height if result > start1 and result < end1 ]
data2=[result for result in height if result > start2 and result < end2 ]
data3=[result for result in height if result > start3 and result < end3 ]
data1P=len(data1)/len(height)*100
data2P=len(data2)/len(height)*100
data3P=len(data3)/len(height)*100
print(data1P)
print(data2P)
print(data3P)

