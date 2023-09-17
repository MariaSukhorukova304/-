#4
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