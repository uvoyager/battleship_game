import pygame as pg
import field
import ships
import menu
import winner

pg.init()
screen = pg.display.set_mode((800, 800))
field_p1 = field.Field()
ship1_1 = ships.Ship(400, 100, 1)
ship1_2 = ships.Ship(480, 100, 1)
ship1_3 = ships.Ship(540, 100, 1)
ship1_4 = ships.Ship(600, 100, 1)
ship2_1 = ships.Ship(550, 170, 2)
ship2_2 = ships.Ship(500, 170, 2)
ship2_3 = ships.Ship(450, 170, 2)
ship3_1 = ships.Ship(500, 250, 3)
ship3_2 = ships.Ship(450, 250, 3)
ship4_1 = ships.Ship(550, 250, 4)
field_p1.ships = [ship1_1, ship1_2, ship1_3, ship1_4, ship2_1, ship2_2, ship2_3, ship3_1, ship3_2, ship4_1]

field_p2 = field.Field()
ship21_1 = ships.Ship(400, 100, 1)
ship21_2 = ships.Ship(480, 100, 1)
ship21_3 = ships.Ship(540, 100, 1)
ship21_4 = ships.Ship(600, 100, 1)
ship22_1 = ships.Ship(550, 170, 2)
ship22_2 = ships.Ship(500, 170, 2)
ship22_3 = ships.Ship(450, 170, 2)
ship23_1 = ships.Ship(500, 250, 3)
ship23_2 = ships.Ship(450, 250, 3)
ship24_1 = ships.Ship(550, 250, 4)
field_p2.ships = [ship21_1, ship21_2, ship21_3, ship21_4, ship22_1, ship22_2, ship22_3, ship23_1, ship23_2, ship24_1]

button_to_2 = menu.Button(300, 700, 'NEXT PLAYER')
button_to_game = menu.Button(300, 700, 'START')
button_menu_game = menu.Button(290, 110, "PLAY")
button_finish_menu= menu.Button(290, 195, "CLOSE")
button_finish_winner = menu.Button(300, 620, 'CLOSE')
current_scene = 'open menu'
fields = [field_p1, field_p2]

running = True
while running:
    if current_scene == 'open menu':
        field = None
        ships = []
    elif current_scene == '1st player':
        field = field_p1
        ships = field_p1.ships
    elif current_scene == '2nd player':
        field = field_p2
        ships = field_p2.ships
    elif current_scene == 'game mode':
        field = None
        ships = []
    elif current_scene == 'game over':
        field = None
        ships = []
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if current_scene == "open menu":
            if button_menu_game.is_clicked(event):
                current_scene = "1st player"
            elif button_finish_menu.is_clicked(event):
                running = False
        elif current_scene == '1st player' and button_to_2.is_clicked(event):
            current_scene = '2nd player'
        elif current_scene == '2nd player' and button_to_game.is_clicked(event):
            field_p1.x, field_p1.y = 50, 200
            field_p2.x, field_p2.y = 450, 200
            current_scene = 'game mode'
        if current_scene == 'game mode' and event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
            field_p1.shot(event.pos)
            field_p2.shot(event.pos)
            if field_p1.check():
                current_scene = 'game over for 1'
            elif field_p2.check():
                current_scene = 'game over for 2'
        if current_scene == 'game over for 1':
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if button_to_game.is_clicked(event):
                    current_scene == 'open menu'
                if button_finish_winner.is_clicked(event):
                    running = False
        elif current_scene == 'game over for 2':
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if button_to_game.is_clicked(event):
                    current_scene == 'open menu'
                if button_finish_winner.is_clicked(event):
                    running = False
        for ship in ships:
            ship.drag(event)
            ship.turn(event)

    menu.draw_background(screen)
    menu.draw_mine(100, 470)
    menu.draw_mine(300, 530)
    menu.draw_mine(520, 500)
    menu.draw_mine(700, 450)
    menu.draw_mine(750, 550)
    menu.draw_mine(400, 620)
    menu.draw_mine(300, 700)
    menu.draw_mine(100, 670)
    menu.draw_mine(700, 720)
    menu.draw_mine(620, 600)
    if current_scene == 'open menu':
        menu.title_text = menu.font.render("ГОЛОВНЕ МЕНЮ", True, menu.DEEP_PURPLE)
        menu.screen.blit(menu.title_text, (210, 25))
        menu.draw_dreadnought_front(400, menu.HORIZON_Y + 5)
        menu.draw_dreadnought_side(160, menu.HORIZON_Y + 5, False)
        menu.draw_dreadnought_side(640, menu.HORIZON_Y + 5, True)
        button_menu_game.draw(screen)
        button_finish_menu.draw(screen)
    elif current_scene == '1st player':
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
    elif current_scene == 'game over for 1':
        t1 = winner.font.render("WINNER", True, winner.DEEP_PURPLE)
        t2 = winner.sub_font.render("PLAYER 2", True, winner.DEEP_PURPLE)
        screen.blit(t1, (winner.SCREEN_WIDTH // 2 - t1.get_width() // 2, 15))
        screen.blit(t2, (winner.SCREEN_WIDTH // 2 - t2.get_width() // 2, 85))
        winner.draw_curved_firework(135, 220, 95)
        winner.draw_curved_firework(665, 220, 95)
        winner.draw_dreadnought_side(130, winner.HORIZON_Y + 5, False)
        winner.draw_dreadnought_side(670, winner.HORIZON_Y + 5, True)
        winner.draw_tk_hamster(400, winner.HORIZON_Y + 15)
        button_finish_winner.draw(screen)
        button_to_game.draw(screen)
    elif current_scene == 'game over for 2':
        t1 = winner.font.render("WINNER", True, winner.DEEP_PURPLE)
        t2 = winner.sub_font.render("PLAYER 1", True, winner.DEEP_PURPLE)
        screen.blit(t1, (winner.SCREEN_WIDTH // 2 - t1.get_width() // 2, 15))
        screen.blit(t2, (winner.SCREEN_WIDTH // 2 - t2.get_width() // 2, 85))
        winner.draw_curved_firework(135, 220, 95)
        winner.draw_curved_firework(665, 220, 95)
        winner.draw_dreadnought_side(130, winner.HORIZON_Y + 5, False)
        winner.draw_dreadnought_side(670, winner.HORIZON_Y + 5, True)
        winner.draw_tk_hamster(400, winner.HORIZON_Y + 15)
        button_finish_winner.draw(screen)
        button_to_game.draw(screen)

    pg.display.update()
pg.quit()
