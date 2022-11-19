import math

def SaveData(str):
    f = open("Output.txt", "a")
    f.write(str+"\n___________________________\n")
    f.close()
def clearData():
    f = open("Output.txt", "w")
    f.write("")
    f.close()
def C(N,M):
    return (Factorial(N)//(Factorial(M)*Factorial(N-M)))
def Factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i
    return factorial

#n - all
#m - positive
#p - chance on positive
def bernulli(n,m,p):
    return C(n,m)*(p**m)*((1-p)**(n-m))
def bernulliSum(n,m1,m2,p):
    s = 0
    for i in range(m1,m2):
        s += bernulli(n,i,p)
    return s
#1
def TrainTask(n,m,p):
    return f'Train Task Result = {bernulli(n,m,p)}'
#2
def ChanceTask(n,m,p):
    return f'Chance Task A Result = {bernulli(n,m,p)}\n' \
           f'Chance Task B Result = {bernulli(n,m,p)+bernulli(n+1,n+1,p)}'
#3
def SugarTask(n,m,p):
    return f'Sugar Task Result = {bernulli(n, m, p)}'
#4
def CarFabric(n,m,p):
    return f'Car Fabric Result = {bernulli(n,m,p)}'
#5
def ItemTask(n,m1,m2,p):
    return f'Item Task Result = {bernulliSum(n,m1,m2,p)}'
#6
def BanTask():
    p = 0.04
    q = 1 - p
    n = 100
    high = p * n + p
    answer = math.floor(high)
    return f'Ban Task Result = {answer}'
def FabricItemsTask(n,m1,m2,p):
    return f'Fabric Items Task Result = {bernulliSum(n,m1,m2,p)}'
def CoinTask(n,m,p):
    return f'Coin Task Result = {bernulli(n,m,p)}'
def BaseTask(n,m,p):
    return f'Base Task Result = {bernulli(n,m,p)}'
def CashTask():
    p = 0.03
    q = 1 - p
    n = 150
    high = p * n + p
    answer = math.floor(high)
    return f'Cash Task Result = {answer}'
clearData()
SaveData(TrainTask(5,3,0.2))
SaveData(ChanceTask(4,3,0.8))
SaveData(SugarTask(400,80,0.2))
SaveData(CarFabric(100000,5,0.0001))
SaveData(ItemTask(600,228,252,0.4))
SaveData(BanTask())
SaveData(FabricItemsTask(4000,1,170,0.04))
SaveData(CoinTask(1000,500,0.5))
SaveData(BaseTask(1000,5,0.002))
SaveData(CashTask())
print()

