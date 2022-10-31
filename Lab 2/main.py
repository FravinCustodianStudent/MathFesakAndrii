import math
import matplotlib.pyplot as plt

from task_02_data.data import Item
f = open("Output.txt","w")
f.write("")
f.close()
def WriteFile(str):
    f = open("Output.txt","a")
    f.write(str)
    f.close()
def getData(fileName,array):
    with open(f'task_02_data/{fileName}', "r") as file:
        for line in file:
            array.append(int(line))
def findPercentile(percentile,data):
    quartValue = ((percentile / 100) * (data.__len__() + 1))
    qValueRounded = int(quartValue)
    value = data[qValueRounded-1]
    return value + (percentile/100 ) * (data[qValueRounded] - data[qValueRounded-1])
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
def StandartDev(data):
    aver = average(data)
    averSquareDeviation = math.sqrt(getDeviation(data))
    element = data[4]
    WriteFile("Standart dev " + str(((element-averSquareDeviation)/aver))+" \n")
def getMutedData(data):
    array1 = []
    for d in data:
        array1.append(0.19*d + 81)
    return array1
def drawSegment(data):
    dates = []
    indexes = []

    for x in range(data.__len__()):
        indexes.append(data[x].name)


    for d in range(data.__len__()):
        if(d==data.__len__()-1):
            break
        if((int(data[d+1].name) -int(data[d].name))>1):
            startData = data[d].name+1
            while(startData<int(data[d+1].name)):
                dates.append(startData)
                startData+=1

    for n in range(dates.__len__()) :
        index = indexes.index(dates[n]-1)
        dat = Item(dates[n],[])
        data.insert(index+1,dat)
    str = ""
    for n in range(data.__len__()):
        str += f'{data[n].name} | '
        if data[n].values != []:
            for d in range(data[n].values.__len__()):
                str += f'{data[n].values[d]} '

        str += "\n"
    str += "\n4|0 = 40 \n "
    return str

def ListDiagram(data):
    Dates = []
    mainDiv = []
    subdiv = []
    for d in data:
        if (int(d/10)) not in mainDiv:
            if mainDiv.__len__() !=0:
                value = int(f'{mainDiv[mainDiv.__len__()-1]}{subdiv[subdiv.__len__()-1]}')
                date: Item = Item(int(value/10),subdiv)
                Dates.append(date)
            subdiv = []
        mainDiv.append(int(d/10))
        subdiv.append(d-int(d/10)*10)
    value = int(f'{mainDiv[mainDiv.__len__() - 1]}{subdiv[subdiv.__len__() - 1]}')
    date = Item(int(value/10),subdiv)
    Dates.append(date)
    return Dates
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
    WriteFile(str(ar) +"\n")

WriteFile("1 quart =" + str(findPercentile(25,data)) +"\n")

WriteFile("3 quart ="+str(findPercentile(75,data)) +"\n")

WriteFile("90 pers ="+str(findPercentile(90,data)) +"\n")

WriteFile("deviation ="+str(math.sqrt(getDeviation(data))) +"\n")

WriteFile("average ="+str(average(data)) +"\n")
StandartDev(data)
WriteFile("_________________________________________________\n")
data2 = getMutedData(data)
for d in data2:
    WriteFile(str(d) +"\n")
WriteFile("_________________________________________________\n")
Dates = ListDiagram(data)
WriteFile(drawSegment(Dates) )
BuildBoxDiagram(data)