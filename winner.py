import pygame
import math
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Winner")

WHITE = (255, 255, 255)
GRID_PURPLE = (235, 230, 250)
DEEP_PURPLE = (90, 60, 150)
SHIP_DARK = (40, 45, 110)
SHIP_LIGHT = (110, 125, 235)
BTN_BLUE = (140, 160, 250)
BTN_HOVER = (180, 195, 255)
PINK_FIREWORK = (245, 110, 165)
GOLD = (255, 215, 0)
SEA_COLOR_TRANSPARENT = (65, 75, 175, 160)

font = pygame.font.SysFont("arialblack", 55)
sub_font = pygame.font.SysFont("arialblack", 32)
btn_font = pygame.font.SysFont("arialblack", 30)
HORIZON_Y = 340


def draw_background():
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
def draw_dreadnought_side(x, y, flip=False):
    d = -1 if flip else 1
    hull_pts = [(x - 100 * d, y), (x + 110 * d, y), (x + 125 * d, y - 25), (x + 50 * d, y - 28), (x - 100 * d, y - 25)]
    pygame.draw.polygon(screen, SHIP_DARK, hull_pts)
    pygame.draw.polygon(screen, SHIP_LIGHT, hull_pts, 2)
    rect_w, rect_h = 100, 18
    rect_x = x - 50
    pygame.draw.rect(screen, SHIP_DARK, (rect_x, y - 43, rect_w, rect_h))
    pygame.draw.rect(screen, SHIP_LIGHT, (rect_x, y - 43, rect_w, rect_h), 1)
    pipe_y = y - 63
    p1_x = x - 25 * d if not flip else x + 10 * d
    pygame.draw.rect(screen, SHIP_DARK, (p1_x, pipe_y, 15, 20))
    pygame.draw.rect(screen, SHIP_LIGHT, (p1_x, pipe_y, 15, 20), 1)
    pygame.draw.line(screen, SHIP_LIGHT, (x + 55 * d, y - 28), (x + 55 * d, y - 90), 2)
    pygame.draw.line(screen, SHIP_LIGHT, (x - 60 * d, y - 25), (x - 60 * d, y - 80), 2)
def draw_curved_firework(x, y, base_radius=90):
    radii_layers = [base_radius * 0.5, base_radius * 0.8, base_radius]
    num_rays = 14
    for radius in radii_layers:
        for i in range(num_rays):
            angle = math.pi + (i * math.pi / (num_rays - 1))
            points = []
            for step in range(11):
                t = step / 10
                px = x + math.cos(angle) * radius * t
                py = y + math.sin(angle) * radius * t + (45 * (t ** 2))
                points.append((px, py))
            pygame.draw.lines(screen, PINK_FIREWORK, False, points, 2)
            if radius == base_radius and (i % 2 == 0):
                pygame.draw.circle(screen, GOLD, (int(points[-1][0]), int(points[-1][1])), 4)
def draw_mine(x, y):
    radius = 18
    for i in range(8):
        angle = i * (math.pi / 4)
        pygame.draw.line(screen, SHIP_DARK, (x, y), (x + math.cos(angle) * 28, y + math.sin(angle) * 28), 3)
    pygame.draw.circle(screen, SHIP_DARK, (x, y), radius)
    pygame.draw.circle(screen, SHIP_LIGHT, (x, y), radius, 2)
    pygame.draw.circle(screen, WHITE, (x - 5, y - 5), 3)
def draw_tk_hamster(cx, cy):
    HAM_BROWN = (217, 160, 102)
    HAM_BEIGE = (248, 240, 230)
    HAM_PINK = (242, 182, 182)
    CHEEK_PINK = (246, 212, 199)
    MUZZLE_WHITE = (255, 245, 235)
    HEART_PINK = (255, 122, 168)
    BLACK = (0, 0, 0)
    s = 0.45
    def draw_oval(color, x1, y1, x2, y2, width=0):
        w = int((x2 - x1) * s)
        h = int((y2 - y1) * s)
        rx = int(cx + (x1 - 400) * s)
        ry = int(cy + (y1 - 430) * s)
        pygame.draw.ellipse(screen, color, (rx, ry, w, h), width)
    draw_oval(CHEEK_PINK, 280, 700, 360, 760);
    draw_oval(BLACK, 280, 700, 360, 760, 2)
    draw_oval(CHEEK_PINK, 440, 700, 520, 760);
    draw_oval(BLACK, 440, 700, 520, 760, 2)
    draw_oval(HAM_BROWN, 220, 280, 580, 760);
    draw_oval(BLACK, 220, 280, 580, 760, 2)
    draw_oval(HAM_BEIGE, 270, 360, 530, 760)
    draw_oval(HAM_BROWN, 180, 110, 270, 210);
    draw_oval(BLACK, 180, 110, 270, 210, 2)
    draw_oval(HAM_BROWN, 530, 110, 620, 210);
    draw_oval(BLACK, 530, 110, 620, 210, 2)
    draw_oval(HAM_PINK, 200, 130, 250, 190);
    draw_oval(HAM_PINK, 550, 130, 600, 190)
    draw_oval(HAM_BROWN, 200, 100, 600, 430);
    draw_oval(BLACK, 200, 100, 600, 430, 2)
    draw_oval(CHEEK_PINK, 220, 240, 320, 320);
    draw_oval(CHEEK_PINK, 480, 240, 580, 320)
    draw_oval(MUZZLE_WHITE, 260, 240, 540, 360)
    draw_oval(BLACK, 280, 210, 340, 270);
    draw_oval(BLACK, 460, 210, 520, 270)
    draw_oval(WHITE, 300, 225, 318, 243);
    draw_oval(WHITE, 480, 225, 498, 243)
    pygame.draw.polygon(screen, HAM_PINK, [(int(cx - 15 * s), int(cy - 145 * s)), (int(cx + 15 * s), int(cy - 145 * s)), (int(cx), int(cy - 120 * s))])
    pygame.draw.polygon(screen, BLACK, [(int(cx - 15 * s), int(cy - 145 * s)), (int(cx + 15 * s), int(cy - 145 * s)), (int(cx), int(cy - 120 * s))], 1)
    r1 = (int(cx - 50 * s), int(cy - 130 * s), int(50 * s), int(50 * s))
    r2 = (int(cx), int(cy - 130 * s), int(50 * s), int(50 * s))
    pygame.draw.arc(screen, BLACK, r1, math.radians(200), math.radians(340), 2)
    pygame.draw.arc(screen, BLACK, r2, math.radians(200), math.radians(340), 2)
    for y_offset in [-15, 0, 15]:
        pygame.draw.line(screen, BLACK, (int(cx - 160 * s), int(cy - 130 * s + y_offset * s)),
                         (int(cx - 70 * s), int(cy - 140 * s + y_offset * s)), 2)
        pygame.draw.line(screen, BLACK, (int(cx + 70 * s), int(cy - 140 * s + y_offset * s)),
                         (int(cx + 160 * s), int(cy - 130 * s + y_offset * s)), 2)
    draw_oval(HEART_PINK, 340, 420, 400, 480)
    draw_oval(HEART_PINK, 400, 420, 460, 480)
    pygame.draw.polygon(screen, HEART_PINK, [(int(cx - 60 * s), int(cy + 20 * s)), (int(cx + 60 * s), int(cy + 20 * s)),
                                             (int(cx), int(cy + 100 * s))])
    draw_oval((255, 0, 0), 340, 420, 400, 480, 2)
    draw_oval((255, 0, 0), 400, 420, 460, 480, 2)
    pygame.draw.polygon(screen, (255, 0, 0),
                        [(int(cx - 60 * s), int(cy + 20 * s)), (int(cx + 60 * s), int(cy + 20 * s)),
                         (int(cx), int(cy + 100 * s))], 2)
    draw_oval(CHEEK_PINK, 285, 390, 375, 480);
    draw_oval(BLACK, 285, 390, 375, 480, 2)
    draw_oval(CHEEK_PINK, 425, 390, 515, 480);
    draw_oval(BLACK, 425, 390, 515, 480, 2)
class Button:
    def __init__(self, x, y, text):
        self.rect = pygame.Rect(x, y, 250, 60)
        self.text = text
        self.hover = False
    def draw(self, surface):
        color = BTN_HOVER if self.hover else BTN_BLUE
        pygame.draw.rect(surface, color, self.rect, border_radius=12)
        pygame.draw.rect(surface, DEEP_PURPLE, self.rect, 3, border_radius=12)
        txt = btn_font.render(self.text, True, DEEP_PURPLE)
        surface.blit(txt, txt.get_rect(center=self.rect.center))
play_btn = Button(275, 410, "ГРАТИ")
exit_btn = Button(275, 495, "ВИХІД")
run = True
while run:
    draw_background()
    t1 = font.render("ПЕРЕМОЖЕЦЬ", True, DEEP_PURPLE)
    t2 = sub_font.render("ГРАВЕЦЬ", True, DEEP_PURPLE)
    screen.blit(t1, (SCREEN_WIDTH // 2 - t1.get_width() // 2, 15))
    screen.blit(t2, (SCREEN_WIDTH // 2 - t2.get_width() // 2, 85))
    draw_curved_firework(135, 220, 95)
    draw_curved_firework(665, 220, 95)
    draw_dreadnought_side(130, HORIZON_Y + 5, False)
    draw_dreadnought_side(670, HORIZON_Y + 5, True)
    draw_tk_hamster(400, HORIZON_Y + 15)
    for p in [(70, 450), (180, 520), (730, 450), (620, 510)]:
        draw_mine(p[0], p[1])
    mouse_pos = pygame.mouse.get_pos()
    for b in [play_btn, exit_btn]:
        b.hover = b.rect.collidepoint(mouse_pos)
        b.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if play_btn.hover: print("Гра почалась!")
            if exit_btn.hover: run = False
    pygame.display.update()
pygame.quit()