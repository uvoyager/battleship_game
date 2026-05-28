import pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
class Ship:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.cell=20
        self.color=(0, 0, 0)
        self.dragg=False
        self.offset_x = 0
        self.offset_y = 0
        self.angle=90
        width = self.cell
        height = self.cell * size
        self.original_surface = pygame.Surface((width + 20, height + 20))
        self.change = self.original_surface
        self.rect = self.change.get_rect(center=(self.x, self.y))
    def draw(self):
        pygame.draw.rect(self.original_surface, self.color,(10, 20, self.cell, self.cell * (self.size - 1)))
        pygame.draw.polygon(self.original_surface, self.color,[(10, 20), (20, 0), (30, 20)])
        screen.blit(self.change, self.rect) # to combine to surfaces basically
    def drag(self, event):
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                self.dragg=True
                mouse_x, mouse_y = event.pos
                self.offset_x = self.rect.x - mouse_x
                self.offset_y = self.rect.y - mouse_y

        elif event.type ==pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.dragg = False

        elif event.type ==pygame.MOUSEMOTION:
            if self.dragg:
                mouse_x, mouse_y = event.pos
                self.rect.x = mouse_x + self.offset_x
                self.rect.y = mouse_y + self.offset_y

    def turn(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.angle += 90
                center = self.rect.center
                self.change = pygame.transform.rotate(
                    self.original_surface,
                    self.angle
                )
                self.rect = self.change.get_rect(center=center)


    # def killed(self):w

class Ship1(Ship):
    def __init__(self, x, y):
        Ship.__init__(self, x, y, 1)

class Ship2(Ship):
    def __init__(self, x, y):
        Ship.__init__(self, x, y, 2)

class Ship3(Ship):
    def __init__(self, x, y):
        Ship.__init__(self, x, y, 3)

class Ship4(Ship):
    def __init__(self, x, y):
        Ship.__init__(self, x, y, 4)


### TEST SHIP
ship = Ship(200, 100, 4)
running = True
while running: # output ship
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        ship.drag(event)
        ship.turn(event)
    screen.fill((255, 255, 255)) # white screen
    ship.draw()
    pygame.display.update()
pygame.quit()
