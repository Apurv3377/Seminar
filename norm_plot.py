#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import sys


filename=str(sys.argv[1])
x, y = np.loadtxt(filename, delimiter=',', unpack=True)
plt.plot(x,y,'ro', label='Loaded from file!')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
