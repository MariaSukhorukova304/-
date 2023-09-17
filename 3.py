#3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-100, 100, 0.001)
plt.plot(x, np.log(x**2 + 1)/np.log(1+np.tan(1/(1+np.sin(x)**2)))*np.exp(abs(x)/(-10)))
plt.show()