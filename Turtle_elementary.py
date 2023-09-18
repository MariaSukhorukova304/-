import turtle

#квадрат
'''
turtle.shape('turtle')
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
'''

#круг
'''
turtle.shape('turtle')
for i in range(360):
    turtle.forward(1)
    turtle.left(1)
'''

#вложенные кавдраты
'''
for i in range(10):
    turtle.pendown()
    for _ in range(3):
        turtle.forward(10*i)
        turtle.right(90)
    turtle.forward(10*i)
    turtle.penup()
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(5)
    turtle.left(180)
'''

#Паук
'''
n = int(input('type number of legs'))
for _ in range(n):
    turtle.forward(150)
    turtle.stamp()
    turtle.right(180)
    turtle.forward(150)
    turtle.right(180)
    turtle.right(360/n)
'''

#Архимедова спираль
'''
from math import pi, sin, cos

turtle.shape('turtle')
for i in range(200):
    t = i / 10 * pi
    dx = t * cos(t)
    dy = t * sin(t)
    turtle.goto(dx, dy)
'''

#Квадратная спираль
'''
for i in range(10):
    for _ in range(2):
        turtle.forward(10 * i)
        turtle.left(90)
        turtle.forward(10 * i)
'''
