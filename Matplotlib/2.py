# 2
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.001)
plt.hlines(0, -10, 10, colors='red')
plt.plot(x, x**2 - x - 6)
plt.show()