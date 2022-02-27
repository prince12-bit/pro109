import statistics
import pandas as pd 
import csv
import plotly.figure_factory as ff 

df = pd.read_csv("stdPerformance.csv")

data = df["reading score"].tolist()


mean = statistics.mean(data)

median = statistics.median(data)

mode = statistics.mode(data)

stdev = statistics.stdev(data)

print("Mean --> " , mean)
print("median --> " , median)
print("mode --> " , mode)
print("stdev --> " , stdev)
print("-----------------------------------------")

fig = ff.create_distplot([data] , ["Graph"] , show_hist = False)
fig.show()

#---------------------------------------------------------------------------------------------

stdevStart1 , stdevEnd1 = mean - stdev , mean + stdev

stdevStart2,  stdevEnd2 = mean -(2 * stdev), mean + (2 * stdev)

stdevStart3,  stdevEnd3 = mean -(3 * stdev), mean + (3 * stdev)

n = len(data)

listOfDataWithin1 = [result for result in data if result > stdevStart1 and result < stdevEnd1]

listOfDataWithin2 = [result for result in data if result > stdevStart2 and result < stdevEnd2]

listOfDataWithin3 = [result for result in data if result > stdevStart3 and result < stdevEnd3]

p1 = (len(listOfDataWithin1) * 100.0 ) / n
p2 = (len(listOfDataWithin2) * 100.0) / n
p3 = (len(listOfDataWithin3) * 100.0) /n

print("Percentage of Data Within 1 standard deviation --> " , p1)
print("Percentage of Data Within 2 standard deviation --> " , p2)
print("Percentage of Data Within 3 standard deviation --> " , p3)
print("-----------------------------------------------------------------------")



