import pygame
class Ship:
    def __init__(self, x, y, size):
        self.size = size
        self.cell = 30
        self.color = 'BROWN'
        self.dragg = False
        self.offset_x = 0
        self.offset_y = 0
        self.angle = 0
        self.board_offset = 70
        self.col = (x - self.board_offset) // self.cell
        self.row = (y - self.board_offset) // self.cell
        width = self.cell
        height = self.cell * size
        self.original_surface = pygame.Surface((width, height))
        self.original_surface.fill(self.color)
        self.change = self.original_surface
        self.rect = self.change.get_rect()
        self.snap_to_grid()
        self.hit_cells = set()
    def snap_to_grid(self):
        pixel_x = self.board_offset + self.col * self.cell
        pixel_y = self.board_offset + self.row * self.cell
        if self.angle in [0, 180]:
            self.rect = self.change.get_rect(topleft=(pixel_x, pixel_y))
        else:
            self.rect = self.change.get_rect(topleft=(pixel_x, pixel_y))
    def draw(self, screen):
        screen.blit(self.change, self.rect)
    def drag(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.dragg = True
                    mouse_x, mouse_y = event.pos
                    self.offset_x = self.rect.x - mouse_x
                    self.offset_y = self.rect.y - mouse_y
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and self.dragg:
                self.dragg = False
                self.col = round((self.rect.x - self.board_offset) / self.cell)
                self.row = round((self.rect.y - self.board_offset) / self.cell)
                self.col = max(0, min(self.col, 10 - (self.size if self.angle in [90, 270] else 1)))
                self.row = max(0, min(self.row, 10 - (1 if self.angle in [90, 270] else self.size)))
                self.snap_to_grid()
        elif event.type == pygame.MOUSEMOTION:
            if self.dragg:
                mouse_x, mouse_y = event.pos
                self.rect.x = mouse_x + self.offset_x
                self.rect.y = mouse_y + self.offset_y
    def turn(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if self.dragg or self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.angle = (self.angle + 90) % 360
                    self.change = pygame.transform.rotate(self.original_surface, self.angle)
                    self.snap_to_grid()
    def get_cells(self):
        cells = []
        if self.angle in [0, 180]:
            for i in range(self.size):
                cells.append((self.col, self.row + i))
        elif self.angle in [90, 270]:
            for i in range(self.size):
                cells.append((self.col + i, self.row))
        return cells
    def get_killed(self):
        for cell in self.get_cells():
            if cell not in self.hit_cells:
                return False
        return True


class Ship1(Ship):
    def __init__(self, x, y): super().__init__(x, y, 1)
class Ship2(Ship):
    def __init__(self, x, y): super().__init__(x, y, 2)
class Ship3(Ship):
    def __init__(self, x, y): super().__init__(x, y, 3)
class Ship4(Ship):
    def __init__(self, x, y): super().__init__(x, y, 4)
