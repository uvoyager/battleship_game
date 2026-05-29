import pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
class Ship:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.cell=30
        self.color="BROWN"
        self.dragg=False
        self.offset_x = 0
        self.offset_y = 0
        self.angle=0
        width = self.cell
        height = self.cell * size
        self.original_surface = pygame.Surface((width, height))
        self.change = self.original_surface
        self.rect = self.change.get_rect(center=(self.x, self.y))
    def draw(self):
        self.original_surface.fill('WHITE')
        pygame.draw.rect(self.original_surface, self.color,(10, 20, self.cell, self.cell * self.size))
        screen.blit(self.change, self.rect) # to combine to surfaces basically
    def drag(self, event):
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                # FIX: Added collidepoint check so you only drag when clicking ON the ship
                if self.rect.collidepoint(event.pos):
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

    def get_cells(self):
        cells = []
        center_x = (self.rect.centerx - 70) // 30
        center_y = (self.rect.centery - 70) // 30

        if self.angle in [0, 180]:
            for i in range(self.size):
                cells.append((center_x, center_y + i))

        elif self.angle in [90, 270]:
            for i in range(self.size):
                cells.append((center_x + i, center_y))
        print(cells)
        return cells

    def get_killed(self, shots):
        ship_cells = self.get_cells()
        shot=True
        for cell in ship_cells:
            if cell not in shots:
                shot=False
        return shot

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
        ship.get_cells()
        ship.get_killed(ship.get_cells())
    screen.fill((255, 255, 255)) # white screen
    ship.draw()
    pygame.display.update()
pygame.quit()
