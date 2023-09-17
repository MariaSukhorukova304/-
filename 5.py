#5
import numpy as np
import matplotlib.pyplot as plt

x = [1.0, 2.0, 3.0, 4.0, 5.0]
y = [0.99, 0.49, 0.35, 0.253, 0.18]
p1 = []
p2 = []

p, v = np.polyfit(x, y, deg=1, cov=True)
p_f = str(np.poly1d(p)).split()
for i in x:
    p1.append(float(p_f[0])*i+float(p_f[3]))
plt.plot(x, p1, color='red', label=r'$Приближение\ по\ многочленам\ 1й\ степени$')

p, v = np.polyfit(x, y, deg=2, cov=True)
p_f = str(np.poly1d(p)).split()
print(p_f)
for i in x:
    p2.append(float(p_f[1])*i - float(p_f[4])*i + float(p_f[-1]))
plt.plot(x, p2, color='green', label=r'$Приближение\ по\ многочленам\ 2й\ степени$')


plt.errorbar(x, y, xerr=0.05, yerr=0.1, color='black')
plt.legend(loc='best', fontsize=9)
plt.grid()
plt.show()
