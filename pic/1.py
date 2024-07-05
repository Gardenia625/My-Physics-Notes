import numpy as np
import math
import matplotlib.pyplot as plt

x = np.arange(-1,3,0.01)
c = -1
y1 = []
for t in x:
    if t <= 0:
        y1.append(100)
    else:
        y_i = 1 / (c + math.exp(t))
        y1.append(y_i)
plt.plot(x, y1, label="Bose-Einstein")
c = 0
y2 = []
for t in x:
    y_i = 1 / (c + math.exp(t))
    y2.append(y_i)
plt.plot(x, y2, label="Maxwell-Boltzmann", linestyle = ":")
c = 1
y3 = []
for t in x:
    y_i = 1 / (c + math.exp(t))
    y3.append(y_i)
plt.plot(x, y3, label="Fermi-Dirac", linestyle = "--")

plt.xlabel("β(ε-μ)", fontsize=20)
plt.xticks(fontsize=20)
plt.ylabel("<n>", fontsize=20)
plt.yticks(fontsize=20)
plt.ylim(-1, 3)
plt.ylim(0, 5)
plt.legend(fontsize=20)
plt.show()