import statistics as stats
import pandas as pd

file= pd.read_csv("StudentsPerformance.csv")
mathsscList= file["math score"].tolist()

mean= stats.mean(mathsscList)
print("The mean is {}".format(mean))

median= stats.median(mathsscList)
print("The median is {}".format(median))

mode= stats.mode(mathsscList)
print("The mode is {}".format(mode))

stdev= stats.stdev(mathsscList)
print("The standard deviation is {}".format(stdev))

minimum= mean- 3*stdev
maximum= mean+ 3*stdev

list=[]

for i in mathsscList:
    if i>minimum and i<maximum:
        list.append(i)

n= len(list)
total= len(mathsscList) 

probability= (n*100)/total

print("{}% of data lies between the third standard deviation".format(probability))