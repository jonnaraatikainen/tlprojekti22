import numpy as np
import matplotlib.pyplot as plt


def randomi():
    random = np.random.randint(min,max,size = (4,3))
    return random


def rows(data):
    numberOfRows = len(data)/3
    numberOfRows = int(numberOfRows)
    return numberOfRows

def matrix(numberOfRows, data):
    datamatrix = np.zeros((numberOfRows,3))
    datamatrix[:,0] = data[0::3]
    datamatrix[:,1] = data[1::3]
    datamatrix[:,2] = data[2::3]
    return datamatrix

def kMeans(random, datamatrix, numberOfRows):
    for k in range(3):
        Counts = np.zeros(4)
        Distances = np.zeros(4)
        dist1 = np.zeros(4)
        centerPointCumulativeSum = np.zeros((4,3))
        avgDistance = np.zeros((4,3))
    
        for i in range(numberOfRows):
            for j in range(4):
                dist = np.abs(np.sqrt(np.power((random[j,0]- datamatrix[i,0]),2) + 
                                np.power((random[j,1]- datamatrix[i,1]),2) + 
                                np.power((random[j,2]- datamatrix[i,2]),2)))
                dist1[j] = dist
                #print(dist)
            pienin = np.argmin(dist1)
            #print("pienin etäisyys", pienin)
            Counts[pienin] += 1
            centerPointCumulativeSum[pienin, 0:3] += datamatrix[i, 0:3]
                    
            for x in range(4):
                if (Counts[x]==0):
                    avgDistance[x] = np.random.randint(min,max,size=3)
                else:
                    avgDistance[x] = (centerPointCumulativeSum[x,:]/Counts[x])
                    avgDistance = np.around(avgDistance, 2)
                
        print("counts",Counts)
        print("keskiarv",avgDistance)

if __name__== '__main__':
    data = np.loadtxt("putty.log")
    datax = data[0::3]
    datay = data[1::3]
    dataz = data[2::3]
    min = np.min(data)
    max = np.max(data)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.scatter(datax, datay, dataz)
    #plt.show()

    random = randomi()
    numberOfRows = rows(data)
    datamatrix = matrix(numberOfRows, data)
    kMeans(random, datamatrix, numberOfRows)

    
    













