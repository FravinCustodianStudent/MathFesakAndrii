def SaveData(str):
    f = open("Output.txt", "a")
    f.write(str)
    f.close()
def clearData():
    f = open("Output.txt", "w")
    f.write("")
    f.close()
def ColorTask():
    return f'{(22+12)/100} probability P(A) - m/n m = 22+12, n = 100'
def C(N,M):
    return (Factorial(N)/(Factorial(M)*Factorial(N-M)))
def Factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i
    return factorial
def BankTask(Amount):
    if Amount>9 and Amount<1:
        return "Error"
    return f'1-({C(Amount,1)})/({C(10,2)}) = {round(1-(C(Amount,1)/(C(10,2))),2)}'
def ManagerTask(Amount):
    if Amount>9 and Amount<1:
        return "Error"
    return f'1-({C(Amount,3)})/({C(10,3)}) = {round(1-(C(Amount,3)/(C(10,3))),2)}'
def MinimarketTask():
    return f'1-0.15-0.25-0.2-0.1 = {round(1-0.15-0.25-0.2-0.1,3)}'
def TrainTask():
    return f'C(2,80)/C(2,120) = {round(C(80,2)/C(120,2),3)}'
def ManifactureTask():
    return f'0.9*0.8 = {round(0.9*0.8,3)}'
def StudentTask():
    Amount = 10
    AmountMark = 20
    Excelent = 3
    Good = 4
    Medium = 2
    Bad = 1
    GoodMark = 16
    MediumMark = 10
    BadMark = 5
    badRes = (Bad/Amount)*(BadMark/AmountMark)*((BadMark-1)/(AmountMark-1))*((BadMark-2)/(AmountMark-2))
    result = Excelent/Amount + (Good/Amount)*(GoodMark/AmountMark)*((GoodMark-1)/(AmountMark-1))*((GoodMark-2)/(AmountMark-2))\
             + (Medium/Amount)*(MediumMark/AmountMark)*((MediumMark-1)/(AmountMark-1))*((MediumMark-2)/(AmountMark-2)) \
             + badRes

    return f'P(A) = {Excelent}/{Amount} * {Amount}/{Amount} * {Amount-1}/{Amount-1} * {Amount-2}/{Amount-2}' \
           f' + {Good}/{Amount} * {GoodMark}/{AmountMark} * {GoodMark - 1}/{AmountMark - 1} * {GoodMark - 2}/{AmountMark - 2}' \
           f' + {Medium}/{Amount} * {MediumMark}/{AmountMark} * {MediumMark-1}/{AmountMark-1} * {MediumMark-2}/{AmountMark-2}' \
           f' + {Bad}/{Amount} * {BadMark}/{AmountMark} * {BadMark-1}/{AmountMark-1} * {BadMark-2}/{AmountMark-2} = {round(result,3)}' \
           f'\np = n /P(A)\n' \
           f'\na = {round((Excelent/Amount)/result,3)} b = {round(badRes/result,3)}'
def FactoryTask():
    FirstLine = 0.4
    SecondLine = 0.3
    ThirdLine = 0.3
    FirstLineProbality = 0.9
    SecondLineProbality = 0.95
    ThirdLineProbality = 0.95
    return f'P(A) = {FirstLine}*{FirstLineProbality} + {SecondLine}*{SecondLineProbality} + {ThirdLine}*{ThirdLineProbality}' \
           f'= {round(FirstLine*FirstLineProbality + SecondLineProbality*SecondLine+ ThirdLine*ThirdLineProbality,4)}'
def IllnessTask():
    Pneumonia = 0.4
    Peritonit = 0.3
    Angina = 0.3
    PneumoniaProbality = 0.8
    PeritonitProbality = 0.7
    AnginaProbality = 0.85
    result = Pneumonia * PneumoniaProbality + Peritonit*PeritonitProbality + Angina*AnginaProbality
    return f'P(A) = {Pneumonia}*{PneumoniaProbality} + {Peritonit}*{PeritonitProbality} + {Angina}*{AnginaProbality} = ' \
           f'{round(result,3)} \n' \
           f'Result = {Peritonit}*{PeritonitProbality}/({round(result,3)}) = {round((Peritonit*PeritonitProbality)/result,3)}'
def ExperienceIssueTask():
    HighQualification = 0.3
    MiddleQualification = 0.7
    HighReliability = 0.9
    MiddleReliability = 0.8
    result = HighReliability*HighQualification + MiddleReliability*MiddleQualification
    return f'P(A) = {HighQualification}*{HighReliability} + {MiddleQualification}*{MiddleReliability} = ' \
           f'{round(result,4)}\n' \
           f'Result = {HighReliability*HighQualification}/{round(result,4)} = {round((HighQualification*HighReliability)/result,3)}'
clearData()
SaveData("__________________________\nTask1\n")
#task1
SaveData(ColorTask()+"\n")
SaveData("__________________________\nTask2\n")
#task2
SaveData(BankTask(8)+"\n")
SaveData("__________________________\nTask3\n")
#task3
SaveData(ManagerTask(8)+"\n")
SaveData("__________________________\nTask4\n")
#task4
SaveData(MinimarketTask()+"\n")
SaveData("__________________________\nTask5\n")
#task5
SaveData(TrainTask()+"\n")
SaveData("__________________________\nTask6\n")
#task6
SaveData(ManifactureTask()+"\n")
SaveData("__________________________\nTask7\n")
#task7
SaveData(StudentTask()+"\n")
SaveData("__________________________\nTask8\n")
#task8
SaveData(FactoryTask()+"\n")
SaveData("__________________________\nTask9\n")
#task9
SaveData(IllnessTask()+"\n")
SaveData("__________________________\nTask10\n")
#task10
SaveData(ExperienceIssueTask()+"\n")