import math
import matplotlib.pyplot as plt

def getData(fileName,array):
    with open(f'task_02_data/{fileName}', "r") as file:
        for line in file:
            array.append(int(line))
def findPercentile(percentile,data):
    quartValue = ((percentile / 100) * (data.count(data) + 1))
    qValueRounded = int(quartValue)
    value = data[qValueRounded]
    return value + (quartValue - qValueRounded) * (data[qValueRounded + 1] - data[qValueRounded])
def average(data):
    res =0
    for d in data:
        res += d
    return res/data.__len__()
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
def getMutedData(data):
    array1 = []
    for d in data:
        array1.append(0.19*d + 81)
    return array1
def drawSegment(arr,n):
    print(f'{n} |',end=" ")
    for d in arr:
        print(f'{d}',end=" ")
    print("")
def ListDiagram(data):
    mainDiv = []
    subdiv = []
    for d in data:
        if (int(d/10)) not in mainDiv:
            if mainDiv.__len__() !=0:
                value = int(f'{mainDiv[mainDiv.__len__()-1]}{subdiv[subdiv.__len__()-1]}')
                drawSegment(subdiv,int(value/10))
            subdiv = []
        mainDiv.append(int(d/10))
        subdiv.append(d-int(d/10)*10)
    value = int(f'{mainDiv[mainDiv.__len__() - 1]}{subdiv[subdiv.__len__() - 1]}')
    drawSegment(subdiv, int(value / 10))
def BuildBoxDiagram(data):
    fig, ax = plt.subplots()
    boxes = [
        {
            'label': "Lab 2",
            'whislo': data[0],  # Bottom whisker position
            'q1': findPercentile(25,data),  # First quartile (25th percentile)
            'med': findPercentile(50,data),  # Median         (50th percentile)
            'q3': findPercentile(75,data),  # Third quartile (75th percentile)
            'whishi': data[data.__len__() - 1],  # Top whisker position
            'fliers': []  # Outliers
        }
    ]
    ax.bxp(boxes, showfliers=False)
    plt.show()
data = []
getData("input_10.txt",data)
data.sort()
for ar in data:
    print(ar)


print("1 quart =" + str(findPercentile(25,data)))
print("3 quart ="+str(findPercentile(75,data)))
print("90 pers ="+str(findPercentile(90,data)))
print("deviation ="+str(math.sqrt(getDeviation(data))))
print("average ="+str(average(data)))
print("_________________________________________________")
data2 = getMutedData(data)
for d in data2:
    print(d)
print("_________________________________________________")
ListDiagram(data)
BuildBoxDiagram(data)