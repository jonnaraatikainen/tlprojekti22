import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def dataread():
    filename = "C:/tlprojekti22/tlprojekti22/jonnandata2.csv"
    data = pd.read_csv(filename, delimiter=" ")
    # print(data)
    return data


def randomi():
    random = np.random.randint(min, max, size=(4, 3))
    return random


def rows(data):
    numberOfRows = len(data)
    numberOfRows = int(numberOfRows)
    # print("numberofrows",numberOfRows)
    return numberOfRows


def matrix(numberOfRows, data):
    datamatrix = np.zeros((numberOfRows, 3))
    datamatrix[:, 0] = data.values[0::, 5]
    datamatrix[:, 1] = data.values[0::, 6]
    datamatrix[:, 2] = data.values[0::, 7]
    position = data.values[0::, 9]
    # print(datamatrix)
    return datamatrix, position


def kMeans(random, datamatrix, numberOfRows, position):
    for k in range(20):
        Counts = np.zeros(4)
        dist1 = np.zeros(4)
        centerPointCumulativeSum = np.zeros((4, 3))
        avgDistance = np.zeros((4, 3))
        flag = np.zeros(4)
        for i in range(numberOfRows):
            for j in range(4):
                dist = np.abs(np.sqrt(np.power((random[j,0]- datamatrix[i,0]),2) +
                              np.power((random[j,1]- datamatrix[i,1]),2) + 
                              np.power((random[j,2]- datamatrix[i,2]),2)))
                dist1[j] = dist
                #print(dist)
            pienin = np.argmin(dist1)
            #print("pienin etäisyys", pienin)
            flag[pienin] = position[i]
            Counts[pienin] += 1
            centerPointCumulativeSum[pienin, 0:3] += datamatrix[i, 0:3]
                    
            for x in range(4):
                if (Counts[x]==0):
                    avgDistance[x] = np.random.randint(min,max,size=3)
                else:
                    avgDistance[x] = (centerPointCumulativeSum[x,:]/Counts[x])
                    avgDistance = np.around(avgDistance, 2)
        print(flag, "flagiii")
        random = avgDistance
        print(avgDistance,"\n")


                
    print("counts",Counts)
    print("keskiarv",avgDistance)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    print(avgDistance)
    ax.scatter(avgDistance[:,0], avgDistance[:,1], avgDistance[:,2], marker="*",color="red",s=200)
    ax.scatter(datamatrix[:, 0],datamatrix[:, 1],datamatrix[:, 2])
    #plt.show()

    headerData = avgDistance
    with open('TransmitterOpiskelijoille\keskipisteet.h', 'w') as f:
        line = "float w[3][6] = {"
        for i in range(4):
            line = line + "{"
            outputThis = np.array2string(headerData[i,:],precision=2,separator=',')
            line = line + outputThis[1:len(outputThis)-1]
            line = line + ","
            line = line + str(flag[i])
            line = line + "}"
        line = line + "}"
        f.write(line)
        f.write('\n')
    f.close()


    

if __name__== '__main__':
    
    
    data = dataread()
    min = np.min(data.values[0::,5:7])
    max = np.max(data.values[0::,5:7])

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    random = randomi()
    numberOfRows = rows(data)
    datamatrix, position = matrix(numberOfRows, data)
    kMeans(random, datamatrix, numberOfRows,position)

    
    












