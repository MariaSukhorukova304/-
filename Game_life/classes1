import pygame as pg


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

class GameOfLife(object):
    w_width, w_height = 600, 600
    finished = False
    FPS = 60
    screen = pg.display.set_mode((w_width, w_height))

    def __init__(self) -> None:
        ...
    
    def run(self) -> None:
        pg.init()
        pg.display.set_caption('Game of Life')
        clock = pg.time.Clock()
        t = 50
        while not self.finished:
            clock.tick(self.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.finished = True
            self.screen.fill(BLACK)
            # Something happening
            
            pg.display.flip()
            pg.time.wait(t)
        pg.quit()