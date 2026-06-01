import pygame as pg
pg.init()
screen = pg.display.set_mode((800, 800))
class Field:
    def __init__(self, x=70, y=70):
        self.ships = []
        self.shots = {}
        self.x = x
        self.y = y
    def draw(self, screen):
        for row in range(10):
            for col in range(10):
                rectangle = pg.Rect(self.x+col*30, self.y+row*30, 30, 30)
                pg.draw.rect(screen, 'WHITE', rectangle)
                pg.draw.rect(screen, "BLACK", rectangle, 1)
                if (col, row) in self.shots:
                    state = self.shots[(col, row)]
                    if state == 'missed':
                        pg.draw.circle(screen, 'BLUE', rectangle.center, 5)
                    elif state == 'hit':
                        pg.draw.circle(screen, 'RED', rectangle.center, 8)
                    elif state == 'killed':
                        pg.draw.rect(screen, 'BLACK', rectangle)

    def inside_board(self, x, y):
        return 0 <= x < 10 and 0 <= y < 10

    def shot(self, mouse_pos):
        mx, my = mouse_pos
        gx = (mx - self.x) // 30
        gy = (my - self.y) // 30
        if not self.inside_board(gx, gy):
            return 'missed'
        if (gx, gy) in self.shots and self.shots[(gx, gy)] == 'killed':
            return 'killed'
        result = 'missed'
        for ship in self.ships:
            if (gx, gy) in ship.get_cells():
                result = 'hit'
                ship.hit_cells.add((gx, gy))
                if ship.get_killed():
                    result = 'killed'
                    for cell in ship.get_cells():
                        self.shots[cell] = 'killed'
                else:
                    self.shots[(gx, gy)] = 'hit'
                break
        if result == 'missed':
            self.shots[(gx, gy)] = 'missed'
        return result
    def check(self):
        if not self.ships:
            return False
        return all(ship.get_killed() for ship in self.ships)
