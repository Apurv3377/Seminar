#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

filename=str(sys.argv[1])
x, y = np.loadtxt(filename, delimiter=',', unpack=True)
df = pd.DataFrame({"x":x, "y":y})
df2=df[df.y >= 10]

plt.plot(df2.x,df2.y, label="Above 10ms")
plt.plot(df.x,df.y,'ro', label='Database Write')

plt.xlabel('Number of Writes')
plt.ylabel('Time in millisec')
plt.title('Performance Test 1')
plt.legend()
plt.show()
