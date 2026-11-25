import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

font1 = {'family':'serif','color':'blue','size':15}
font2 = {'family':'serif','color':'darkred','size':10}


plt.subplot(2, 1, 1)
#the figure has 1 row, 2 columns, and this plot is the first plot.
plt.title("Hello World graph", fontdict = font1)
plt.xlabel("x values", fontdict = font2)
plt.ylabel("y values", fontdict = font2)
plt.grid()
plt.plot(x1,y1)

plt.subplot(2, 1, 2)
#the figure has 1 row, 2 columns, and this plot is the second plot.
plt.title("The other graph", fontdict = font1)
plt.xlabel("x values", fontdict = font2)
plt.ylabel("y values", fontdict = font2)
plt.grid()
plt.plot(x2, y2)

plt.suptitle("The main title")
plt.show()