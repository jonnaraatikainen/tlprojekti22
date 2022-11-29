import numpy as np
import matplotlib.pyplot as plt


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








