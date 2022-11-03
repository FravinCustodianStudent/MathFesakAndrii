import math
import math as m
import os

import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from sympy import *

from Customer import Customer


def ReadFile(fileName):
    date = []
    file = open(f'task_03_data/{fileName}','r')
    for line in file:
        customer = Customer(float(line[0:line.find('\t')].replace(',', '.')),
                            int(line[line.find('\t') + 1:line.__len__()]))
        date.append(customer)
    return date
def GetAverage(data):
    average = 0
    for d in data:
        average +=d
    return average/data.__len__()
def Covariacion(dataAmount, dataTime, averageAmount, averageTime):
    cov = 0
    for i in range(dataAmount.__len__()):
        cov += (dataAmount[i] - averageAmount)* (dataTime[i] - averageTime)
    return cov/dataAmount.__len__()
def getDeviation(data):
    res = 0
    average = 0
    for d in data:
        res += math.pow(d,2)
        average += d
    average /= data.__len__()
    res /= data.__len__()
    res -= average * average
    return res
def GetM(dataAmount, dataTime, averageAmount, averageTime):
    return float(Covariacion(dataAmount
                             ,dataTime,
                             averageAmount,
                             averageTime)/getDeviation(dataAmount))
def GetK(M, averageAmount, averageTime):
    return averageTime - M*averageAmount
def clearData():
    f = open("Output.txt", "w")
    f.write("")
    f.close()
def SaveData(str):
    f = open("Output.txt", "a")
    f.write(str)
    f.close()
def GetTrend(corelation):
    if corelation > 0:
        return "Trend is positive"
    elif corelation < 0:
        return "Trend is negative"
    else: return "Trend is missing"
def Corelation(dataAmount, dataTime, Covariation):
    dispX = getDeviation(dataAmount)
    dispY = getDeviation(dataTime)
    return Covariation / sqrt(dispX * dispY)
def ScatterPlot(data):
    clearData()
    plt.xticks(np.arange(0,10, step = 0.5))
    plt.yticks(np.arange(0,100, step = 5))

    dataAmount = []
    dataTime = []
    for d in data:
        dataAmount.append(d.Amount)
        dataTime.append(d.Time)

    # TODO: simplify that by send data am/dt
    AverageAmount = GetAverage(dataAmount)
    AverageTime = GetAverage(dataTime)

    DeviationX = getDeviation(dataAmount)
    M = GetM(dataAmount, dataTime, AverageAmount, AverageTime)
    K = GetK(M, AverageAmount, AverageTime)
    Y = []
    for i in range(len((dataAmount))):
        Y.append(dataAmount[i] * M + K)


    corelation = Corelation(dataAmount,dataTime,Covariacion(dataAmount
                         , dataTime,
                         AverageAmount,
                         AverageAmount))
    trendResult = str(GetTrend(corelation))
    plt.plot(dataAmount, Y,
             label=f'{trendResult}',color="red")
    plt.scatter(dataAmount,dataTime,10,label="scatter")
    plt.xlabel("Amount")
    plt.ylabel("Time")
    plt.legend(loc="best")
    plt.show()

    SaveData(
        f'Center of weight is G:({round(AverageAmount,3)};{round(AverageTime,3)})\n'
    f'Covariation is {round(Covariacion(dataAmount,dataTime,AverageAmount,AverageAmount),3)}\n'
    f'Reggression l ine is y ={round(M,3)}x + {round(K,3)}\n'
    f'Corelation {round(corelation,3)}'
    )



#TODO: input for file choose
choise = input("Input FileName: ")
data = ReadFile(choise)

ScatterPlot(data)