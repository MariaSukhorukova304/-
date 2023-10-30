import pygame as pg

pg.init()
fps = 30
width, height = 1000, 1000
window = pg.display.set_mode((width, height))
finished = False
clock = pg.time.Clock()

r_width = 100
r_height = 200
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
vx = 5
vy = 5

def drawRect(x: float, y: float) -> None:
    pg.draw.rect(window, GREEN, (x, y, r_width, r_height))

x = 0
y = 0
while not finished:
    clock.tick(fps)
    window.fill(BLACK)
    drawRect(x, y)
    x += vx
    y += vy
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
    pg.display.flip()
    
pg.quit()
