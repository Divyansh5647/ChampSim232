import numpy as np
import math
import matplotlib.pyplot as plt

def func1(size):
    # print(20*int(math.log2(size/(2048*16) + 1)))
    return int(20*(math.log2(size/(2048*16) + 1)))
def func2(size):
    slope = 512*4
    return 20 + (size-2048*16)/slope

def func3(size):
    slope = 512*8
    return 20 + (size-2048*16)/slope

def func4(size):
    slope = 512*16
    return 20 + (size-2048*16)/slope

def func5(size):
    slope = 512*32
    return 20 + (size-2048*16)/slope

def func6(size):
    slope = 512*64
    return 20 + (size-2048*16)/slope

x = np.linspace(32000,200000,50)
y1=np.zeros(50)
for i in range(50):
    y1[i] = func1(x[i])
# y1= func1(x)
y2 = func2(x)
y3 = func3(x)
y4 = func4(x)
y5 = func5(x)
y6 = func6(x)


plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.plot(x,y5)
plt.plot(x,y6)


plt.legend(["log","slope 1/512*4", "slope 1/512*8", "slope 1/512*16", "slope 1/512*32","slope 1/512*64"])
plt.show()




