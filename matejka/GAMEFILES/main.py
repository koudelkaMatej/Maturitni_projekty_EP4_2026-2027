import pygame
import sys
from settings import *
from menu import Menu

# zapnuti pygame a nastaveni okna
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("OUT OF RAM")
clock = pygame.time.Clock()

# pismo pro zatim nedodelana okna
menu = Menu(screen)
font_placeholder = pygame.font.SysFont("Courier New", 24, bold=True)

#rizeni stavu - menu, hra, nastaveni
game_state = "MENU"


#smycka
running = True
while running:
    # zpracovani jednotilych udalosti
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #kdyz uzivatel zavre okno
            running = False

        #  udalosti dostavaji tlacitka a zjisteni stavu
        if game_state == "MENU":
            new_state = menu.handle_event(event)
            if new_state == "EXIT":
                running = False
            elif new_state in ["GAME", "SETTINGS"]:
                game_state = new_state

        # esc - zpatky z oken
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if game_state in ["GAME", "SETTINGS"]:
                    game_state = "MENU"

    # vykresleni oken podle udalosti
    # menu
    if game_state == "MENU":
        menu.draw()

    #hra
    elif game_state == "GAME":
        screen.fill(COLOR_BG)
        txt = font_placeholder.render("TBD", True, COLOR_TEXT)
        screen.blit(txt, txt.get_rect(center=(400, 300)))

    #nastaveni
    elif game_state == "SETTINGS":
        screen.fill((26, 26, 26))
        txt = font_placeholder.render("TBD", True, COLOR_TEXT)
        screen.blit(txt, txt.get_rect(center=(400, 300)))

    # obnovovani aby to fungovalo
    pygame.display.flip()
    clock.tick(60)

# konec smycky
pygame.quit()
sys.exit()


