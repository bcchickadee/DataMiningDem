#수능특강 독서 과학기술 11번 지문 (데이터 마이닝) 설명 프로그램
#제작: 윤수민, 이정진, 2020년 7월 31일

import random
import matplotlib.pyplot as plt
import statistics

print('수능특강 독서 과학기술 11번 지문 (데이터 마이닝) 설명 프로그램')
print('제작: 윤수민, 이정진, 2020년 7월 31일\n')

FirstX=[]
FirstY=[]
SecondX=[]
SecondY=[]
AllX=[]
AllY=[]

while True:
    FirstCenter=float(input('1번째 집단의 중심 좌표 (기본값 (10, 10)): ') or 10)
    SecondCenter=float(input('2번째 집단의 중심 좌표 (기본값 (-10, -10)): ') or -10)
    FirstDotNum=int(input('1번째 집단 점 개수 (기본값 30개): ') or 30)
    SecondDotNum=int(input('2번째 집단 점 개수 (기본값 30개): ') or 30)
    FirstSigma=float(input('1번째 집단 표준편차 (기본값 5): ') or 5)
    SecondSigma=float(input('2번째 집단 표준편차 (기본값 5): ') or 5)
    ImprovisationNum=int(input('보정 횟수 (기본값 1000번): ') or 1000)
    GroupingNum=int(input('1회 보정 시 선택되는 점 개수 (기본값 15): ') or 15)

    for i in range(FirstDotNum):
        x=random.gauss(FirstCenter, FirstSigma)
        y=random.gauss(FirstCenter, FirstSigma)
        FirstX.append(x)
        FirstY.append(y)
        AllX.append(x)
        AllY.append(y)
        plt.plot(x, y, "bo")

    for i in range(SecondDotNum):
        x=random.gauss(SecondCenter, SecondSigma)
        y=random.gauss(SecondCenter, SecondSigma)
        SecondX.append(x)
        SecondY.append(y)
        AllX.append(x)
        AllY.append(y)
        plt.plot(x, y, "bo")

    FirstXLocalAverage=statistics.mean(random.sample(population=FirstX, k=GroupingNum))
    FirstYLocalAverage=statistics.mean(random.sample(population=FirstY, k=GroupingNum))
    for i in range(ImprovisationNum):
        FirstXTempAverage=statistics.mean(random.sample(population=FirstX, k=GroupingNum))
        if abs(FirstXLocalAverage-FirstCenter)>=abs(FirstXTempAverage-FirstCenter):
            FirstXTempAverage=FirstXLocalAverage
        elif abs(FirstXLocalAverage-FirstCenter)<abs(FirstXTempAverage-FirstCenter):
            del(FirstXTempAverage)

    for i in range(ImprovisationNum):
        FirstYTempAverage=statistics.mean(random.sample(population=FirstY, k=GroupingNum))
        if abs(FirstYLocalAverage-FirstCenter)>=abs(FirstYTempAverage-FirstCenter):
            FirstYTempAverage=FirstYLocalAverage
        elif abs(FirstYLocalAverage-FirstCenter)<abs(FirstYTempAverage-FirstCenter):
            del(FirstYTempAverage)

    plt.plot(FirstXLocalAverage, FirstYLocalAverage, "rx")
    print('\n\n=====================================')
    print('첫번째 집단의 분포')
    print('평균: X: '+str(FirstXLocalAverage)+', Y: '+str(FirstYLocalAverage))

    SecondXLocalAverage=statistics.mean(random.sample(population=SecondX, k=GroupingNum))
    SecondYLocalAverage=statistics.mean(random.sample(population=SecondY, k=GroupingNum))
    for i in range(ImprovisationNum):
        SecondXTempAverage=statistics.mean(random.sample(population=SecondX, k=GroupingNum))
        if abs(SecondXLocalAverage-SecondCenter)>=abs(SecondXTempAverage-SecondCenter):
            SecondXTempAverage=SecondXLocalAverage
        elif abs(SecondXLocalAverage-SecondCenter)<abs(SecondXTempAverage-SecondCenter):
            del(SecondXTempAverage)

    for i in range(ImprovisationNum):
        SecondYTempAverage=statistics.mean(random.sample(population=SecondY, k=GroupingNum))
        if abs(SecondYLocalAverage-SecondCenter)>=abs(SecondYTempAverage-SecondCenter):
            SecondYTempAverage=SecondYLocalAverage
        elif abs(SecondYLocalAverage-SecondCenter)<abs(SecondYTempAverage-SecondCenter):
            del(SecondYTempAverage)

    plt.plot(SecondXLocalAverage, SecondYLocalAverage, "rx")
    print('두번째 집단의 분포')
    print('평균: X: '+str(SecondXLocalAverage)+', Y: '+str(SecondYLocalAverage))

    AllXLocalAverage=statistics.mean(random.sample(population=AllX, k=GroupingNum))
    AllYLocalAverage=statistics.mean(random.sample(population=AllY, k=GroupingNum))
    for i in range(2*ImprovisationNum):
        AllXTempAverage=statistics.mean(random.sample(population=AllX, k=GroupingNum))
        if abs(AllXLocalAverage-(((FirstCenter)+(SecondCenter))/2))>=abs(AllXTempAverage-(((FirstCenter)+(SecondCenter))/2)):
            AllXTempAverage=AllXLocalAverage
        elif abs(AllXLocalAverage-(((FirstCenter)+(SecondCenter))/2))<abs(AllXTempAverage-(((FirstCenter)+(SecondCenter))/2)):
            del(AllXTempAverage)

    for i in range(2*ImprovisationNum):
        AllYTempAverage=statistics.mean(random.sample(population=AllY, k=GroupingNum))
        if abs(AllYLocalAverage-(((FirstCenter)+(SecondCenter))/2))>=abs(AllYTempAverage-(((FirstCenter)+(SecondCenter))/2)):
            AllYTempAverage=AllYLocalAverage
        elif abs(AllYLocalAverage-(((FirstCenter)+(SecondCenter))/2))<abs(AllYTempAverage-(((FirstCenter)+(SecondCenter))/2)):
            del(AllYTempAverage)

    plt.plot(AllXLocalAverage, AllYLocalAverage, "gx")
    print('전체 집단의 분포')
    print('평균: X: '+str(AllXLocalAverage)+', Y: '+str(AllYLocalAverage))

    plt.plot((((FirstCenter)+(SecondCenter))/2), (((FirstCenter)+(SecondCenter))/2), "gP")
    plt.plot(FirstCenter, FirstCenter, "rP")
    plt.plot(SecondCenter, SecondCenter, "rP")

    plt.title("Distribution of "+str(FirstDotNum+SecondDotNum)+" dots")
    plt.show()

    print('\n=====================================')
    print('프로그램을 다시 시작합니다.')
    print('\n=====================================\n\n')
    del FirstCenter
    del SecondCenter
    del FirstDotNum
    del SecondDotNum
    del FirstSigma
    del SecondSigma
    del ImprovisationNum
    del GroupingNum
    
