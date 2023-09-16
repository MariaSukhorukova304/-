# 1

"""
import numpy as np
x = 0
y = np.log((1/(np.e*np.sin(x+1)))/(1.25+(1/x**15)))/np.log(1+x**2)
print(y)
"""

# Theory
"""
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10, 0.001)  #numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None)
plt.plot(x, x**2, x, np.sin(x))
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'$f_1(x)=\sin(x),\ f_2(x)=x**2$')  #could be replased: plt.plot(x, np.sin(x), label=r'$f_1(x)=\sin(x)$')
plt.grid(True)
plt.show()
"""
# 2

'''
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.001)
plt.hlines(0, -10, 10, colors='red')
plt.plot(x, x**2 - x - 6)
plt.show()
'''

#3
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-100, 100, 0.001)
plt.plot(x, np.log(x**2 + 1)/np.log(1+np.tan(1/(1+np.sin(x)**2)))*np.exp(abs(x)/(-10)))
plt.show()
'''

#4
'''
import numpy as np
import matplotlib.pyplot as plt

#data = input().split('')
plt.figure(num=1, figsize=(6, 6))
plt.axes(aspect=1)
with plt.xkcd():
    piesize = [int(a) for a in input('Введите процентное соотношение через пробел').split()]
    labelsin = input('Введите подписи через ";"').split(';')

    plt.pie(piesize, labels=labelsin)
    plt.title(input('О чём диаграмма?'))

n = 'plt.show()'
eval(n) #искренне не понимаю, что нужно делать с использованием eval()
'''

#5
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [0.99, 0.49, 0.35, 0.253, 0.18]
xx = []
yy = []
for i in range(len(x)):
    p, v = np.polyfit(x, y, deg=1, cov=True)
    p_f = str(np.poly1d(p)).split()
    
    print(float(p_f[0]))
plt.plot(x, float(p_f[0])*x+float(p_f[3]))
plt.errorbar(x, y, xerr=0.05, yerr=0.1)
plt.grid()
plt.show()

