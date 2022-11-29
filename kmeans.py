import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as la


data = np.loadtxt("putty.log")
datax = data[0::3]
datay = data[1::3]
dataz = data[2::3]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.scatter(datax, datay, dataz)
plt.show()


numberOfRows = len(data)/3
numberOfRows = int(numberOfRows)
print(numberOfRows)
min = np.min(data)
max = np.max(data)

random = np.random.randint(min,max,size = (4,3))
print(random)

centerPointCumulativeSum = np.zeros((4,3))


Counts = np.zeros((1,4))
Distances = np.zeros((1,4))

'''
a = np.array((2,4,6))
b = np.array((1,2,3))
etaisyys = np.linalg.norm(a-b)

a = np.array(random)
b = np.array(random)
etaisyys = np.linalg.norm(a-b)
print(etaisyys)
'''
datamatrix = np.zeros((numberOfRows,3))
datamatrix[:,0] = datax
datamatrix[:,1] = datay
datamatrix[:,2] = dataz


for i in range(numberOfRows):
    for j in range(4):
        dist = np.sqrt(np.power((random[j,0]- datamatrix[j,0]),2) + 
                       np.power((random[j,1]- datamatrix[j,1]),2) + 
                       np.power((random[j,2]- datamatrix[j,2]),2))
        print(dist)
        












