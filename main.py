import pygame as pg
import field1
import ships1
class Button:
    def __init__(self, x, y, width, height, base_colour, hover_colour, text, text_colour):
        self.rect = pg.Rect(x, y, width, height)
        self.text = text
        self.base_colour = base_colour
        self.hover_colour = hover_colour
        self.font = pg.font.SysFont("monserrat", 20)
        self.text_colour = text_colour
        self.text_surf = self.font.render(self.text, True, self.text_colour)
        self.text_rect = self.text_surf.get_rect(center = self.rect.center)
        self.current_colour = self.base_colour
    def draw(self, screen):
        mouse_pos = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.current_colour = self.hover_colour
        else:
            self.current_colour = self.base_colour
        pg.draw.rect(screen, self.current_colour, self.rect, border_radius = 3)
        screen.blit(self.text_surf, self.text_rect)
    def is_clicked(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
            else:
                return False

pg.init()
screen = pg.display.set_mode((800, 800))
field_p1 = field1.Field()
ship1_1 = ships1.Ship(400, 100, 1)
ship1_2 = ships1.Ship(480, 100, 1)
ship1_3 = ships1.Ship(540, 100, 1)
ship1_4 = ships1.Ship(600, 100, 1)
ship2_1 = ships1.Ship(550, 170, 2)
ship2_2 = ships1.Ship(500, 170, 2)
ship2_3 = ships1.Ship(450, 170, 2)
ship3_1 = ships1.Ship(500, 250, 3)
ship3_2 = ships1.Ship(450, 250, 3)
ship4_1 = ships1.Ship(550, 250, 4)
field_p1.ships = [ship1_1, ship1_2, ship1_3, ship1_4, ship2_1, ship2_2, ship2_3, ship3_1, ship3_2, ship4_1]

field_p2 = field1.Field()
ship21_1 = ships1.Ship(400, 100, 1)
ship21_2 = ships1.Ship(480, 100, 1)
ship21_3 = ships1.Ship(540, 100, 1)
ship21_4 = ships1.Ship(600, 100, 1)
ship22_1 = ships1.Ship(550, 170, 2)
ship22_2 = ships1.Ship(500, 170, 2)
ship22_3 = ships1.Ship(450, 170, 2)
ship23_1 = ships1.Ship(500, 250, 3)
ship23_2 = ships1.Ship(450, 250, 3)
ship24_1 = ships1.Ship(550, 250, 4)
field_p2.ships = [ship21_1, ship21_2, ship21_3, ship21_4, ship22_1, ship22_2, ship22_3, ship23_1, ship23_2, ship24_1]

button_to_2 = Button(300, 700, 150, 30, 'CYAN','LIGHTBLUE',
                'next player\'s field', 'BLACK')
button_to_game = Button(300, 700, 150, 30, 'CYAN','LIGHTBLUE',
                'Start the Game', 'BLACK')
current_scene = '1st player'
fields = [field_p1, field_p2]

running = True
while running:
    if current_scene == '1st player':
        field = field_p1
        ships = field_p1.ships
    elif current_scene == '2nd player':
        field = field_p2
        ships = field_p2.ships
    elif current_scene == 'game mode':
        field = None
        ships = []
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if current_scene == '1st player' and button_to_2.is_clicked(event):
            current_scene = '2nd player'
        elif current_scene == '2nd player' and button_to_game.is_clicked(event):
            field_p1.x, field_p1.y = 50, 200
            field_p2.x, field_p2.y = 450, 200
            current_scene = 'game mode'
        if current_scene == 'game mode' and event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
            field_p1.shot(event.pos)
            field_p2.shot(event.pos)
        for ship in ships:
            ship.drag(event)
            ship.turn(event)
    screen.fill("WHITE")
    if current_scene == '1st player':
        field_p1.draw(screen)
        for ship in field_p1.ships:
            ship.draw(screen)
        button_to_2.draw(screen)
    elif current_scene == '2nd player':
        field_p2.draw(screen)
        for ship in field_p2.ships:
            ship.draw(screen)
        button_to_game.draw(screen)
    elif current_scene == 'game mode':
        for field in fields:
            field.draw(screen)
    pg.display.update()
pg.quit()
