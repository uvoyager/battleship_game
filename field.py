import pygame as pg
class Field:
    def __init__(self):
        self.shots = {}
    def draw(self, screen):
        for row in range(10):
            for col in range(10):
                rectangle = pg.Rect(100+col*50, 100+row*50, 50, 50)
                pg.draw.rect(screen, 'BLUE', rectangle)
                pg.draw.rect(screen, "BLACK", rectangle, 1)
                if (col, row) in self.shots:
                    hit = self.shots[(col, row)]
                    color = 'RED' if hit else 'BLUE'
                    pg.draw.rect(screen, color, rectangle)

    def inside_board(self, x, y):
        return 0 <= x < 10 and 0 <= y < 10
    #def positions(self, ship):

a = Field()
