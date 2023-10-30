import pygame as p
from pygame.locals import *

# Константы цветов RGB
BLACK = (0 , 0 , 0)
WHITE = (255 , 255 , 255)
# Создаем окно
p.init()
fps = 30
width, height = 700, 700
window = p.display.set_mode((width, height))
finished = False
clock = p.time.Clock()


# Основной цикл
while 1:
    # Заполняем экран белым цветом
    window.fill(WHITE)
    
    # Рисуем сетку
    for i in range(0 , window.get_height() // 20):
        p.draw.line(window , BLACK , (0 , i * 20) , (window.get_width() , i * 20))
    for j in range(0 , window.get_width() // 20):
        p.draw.line(window , BLACK , (j * 20 , 0) , (j * 20 , window.get_height()))
    # Нужно чтобы виндовс не думал что программа "не отвечает"
    for i in p.event.get():
        if i.type==	QUIT:
          quit()
    p.display.update()

# 2х мерный список с помощью генераторных выражений
cells=[ [0 for j in range(window.get_width()//20)] for i in range(window.get_height()//20)]  #all cells are filled with initial 0
cells2=cells
# Функция определения кол-ва соседей
def near(pos: list , system=[[-1 , -1] , [-1 , 0] , [-1 , 1] , [0 , -1] , [0 , 1] , [1 , -1] , [1 , 0] , [1 , 1]]):
    count = 0
    for i in system:
        if cells[(pos[0] + i[0]) % len(cells)][(pos[1] + i[1]) % len(cells[0])]:  #?????
            count += 1
    return count


# Проходимся по всем клеткам
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            # Если клетка жива
            if cells[i][j]:
                # Если у соседей не 2 или 3 соседа
                if near([i , j]) not in (2 , 3):
                    cells2[i][j] = 0
                    continue
                # В ином случае
                cells2[i][j] = 1
                continue
            # Если клетка мертва и у неё 3 соседа    
            if near([i , j]) == 3:
                cells2[i][j] = 1
                continue
            # В противном случае    
            cells2[i][j] = 0
    cells = cells2