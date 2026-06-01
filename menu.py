import pygame
import math
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Морський Бій")
WHITE = (255, 255, 255)
GRID_PURPLE = (235, 230, 250)
DEEP_PURPLE = (90, 60, 150)
SHIP_DARK = (40, 45, 110)
SHIP_LIGHT = (110, 125, 235)
BTN_BLUE = (140, 160, 250)
BTN_HOVER = (180, 195, 255)
SEA_COLOR_TRANSPARENT = (65, 75, 175, 160)
font = pygame.font.SysFont("arialblack", 45)
btn_font = pygame.font.SysFont("arialblack", 30)
HORIZON_Y = 340
def draw_background(screen):
    screen.fill(WHITE)
    grid_size = 25
    for x in range(0, SCREEN_WIDTH, grid_size):
        pygame.draw.line(screen, GRID_PURPLE, (x, 0), (x, SCREEN_HEIGHT), 1)
    for y in range(0, SCREEN_HEIGHT, grid_size):
        pygame.draw.line(screen, GRID_PURPLE, (0, y), (SCREEN_WIDTH, y), 1)
    sea_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT - HORIZON_Y), pygame.SRCALPHA)
    sea_surface.fill(SEA_COLOR_TRANSPARENT)
    screen.blit(sea_surface, (0, HORIZON_Y))
    pygame.draw.line(screen, DEEP_PURPLE, (0, HORIZON_Y), (SCREEN_WIDTH, HORIZON_Y), 3)
def draw_dreadnought_front(x, y):
    hull_pts = [(x, y), (x - 35, y - 8), (x - 30, y - 45), (x + 30, y - 45), (x + 35, y - 8)]
    pygame.draw.polygon(screen, SHIP_DARK, hull_pts)
    pygame.draw.polygon(screen, SHIP_LIGHT, hull_pts, 2)
    pygame.draw.rect(screen, SHIP_DARK, (x - 18, y - 70, 36, 25))
    pygame.draw.rect(screen, SHIP_LIGHT, (x - 18, y - 70, 36, 25), 2)
    pygame.draw.line(screen, SHIP_LIGHT, (x, y - 70), (x, y - 120), 2)
    pygame.draw.line(screen, SHIP_LIGHT, (x - 15, y - 100), (x + 15, y - 100), 2)
    pygame.draw.rect(screen, SHIP_DARK, (x - 12, y - 55, 24, 10))
    pygame.draw.line(screen, SHIP_LIGHT, (x, y - 50), (x, y - 15), 3)
def draw_dreadnought_side(x, y, flip=False):
    d = -1 if flip else 1
    hull_pts = [(x - 100 * d, y), (x + 110 * d, y), (x + 125 * d, y - 25), (x + 50 * d, y - 28), (x - 100 * d, y - 25)]
    pygame.draw.polygon(screen, SHIP_DARK, hull_pts)
    pygame.draw.polygon(screen, SHIP_LIGHT, hull_pts, 2)
    rect_w = 100
    rect_h = 18
    rect_x = x - 50
    pygame.draw.rect(screen, SHIP_DARK, (rect_x, y - 43, rect_w, rect_h))
    pygame.draw.rect(screen, SHIP_LIGHT, (rect_x, y - 43, rect_w, rect_h), 1)
    pipe_y = y - 63
    p1_x = x - 25 * d if not flip else x + 10 * d
    pygame.draw.rect(screen, SHIP_DARK, (p1_x, pipe_y, 15, 20))
    pygame.draw.rect(screen, SHIP_LIGHT, (p1_x, pipe_y, 15, 20), 1)
    p2_x = x + 10 * d if not flip else x - 25 * d
    pygame.draw.rect(screen, SHIP_DARK, (p2_x, pipe_y, 15, 20))
    pygame.draw.rect(screen, SHIP_LIGHT, (p2_x, pipe_y, 15, 20), 1)
    pygame.draw.line(screen, SHIP_LIGHT, (x + 55 * d, y - 28), (x + 55 * d, y - 90), 2)
    pygame.draw.line(screen, SHIP_LIGHT, (x - 60 * d, y - 25), (x - 60 * d, y - 80), 2)
    b_x = x + 75 if not flip else x - 100
    pygame.draw.ellipse(screen, SHIP_DARK, (b_x, y - 35, 25, 12))
    pygame.draw.ellipse(screen, SHIP_LIGHT, (b_x, y - 35, 25, 12), 1)
    gun_start_x = b_x + 25 if not flip else b_x
    gun_end_x = gun_start_x + 30 if not flip else gun_start_x - 30
    pygame.draw.line(screen, SHIP_LIGHT, (gun_start_x, y - 29), (gun_end_x, y - 29), 3)
def draw_mine(x, y):
    radius = 18
    for i in range(8):
        angle = i * (math.pi / 4)
        x2 = x + math.cos(angle) * 28
        y2 = y + math.sin(angle) * 28
        pygame.draw.line(screen, SHIP_DARK, (x, y), (x2, y2), 3)
    pygame.draw.circle(screen, SHIP_DARK, (x, y), radius)
    pygame.draw.circle(screen, SHIP_LIGHT, (x, y), radius, 2)
    pygame.draw.circle(screen, WHITE, (x - 5, y - 5), 3)
class Button:
    def __init__(self, x, y, text):
        self.rect = pygame.Rect(x, y, 220, 60)
        self.text = text
        self.hover = False
    def draw(self, surface):
        color = BTN_HOVER if self.hover else BTN_BLUE
        pygame.draw.rect(surface, color, self.rect, border_radius=12)
        pygame.draw.rect(surface, DEEP_PURPLE, self.rect, 3, border_radius=12)
        text_surf = btn_font.render(self.text, True, DEEP_PURPLE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
            else:
                return False
