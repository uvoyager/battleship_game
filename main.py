import pygame as pg
import field1
import ships1
pg.init()
screen = pg.display.set_mode((800, 800))
field = field1.Field()
ship = ships1.Ship(550, 200, 2)
field.ships.append(ship)
running = True
while running:
    screen.fill('WHITE')
    field.draw(screen)
    ship.draw(screen)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        ship.drag(event)
        ship.turn(event)
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 3:
                field.shot(event.pos)
                ship.get_killed()
    pg.display.update()
pg.quit()
