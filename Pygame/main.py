from settings import *
import pygame
import sys

# pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("NEON//GHOST")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
title_font = pygame.font.SysFont(None, 120)

grid_offset = 0  # posun vodorovných čar mřížky (aby se pozadí hýbalo)


def draw_text(text, x, y, color=white, center=False, use_font=None):
    use_font = use_font or font
    text_obj = use_font.render(text, True, color)
    text_rect = text_obj.get_rect()
    if center:
        text_rect.center = (x, y)
        screen.blit(text_obj, text_rect)
    else:
        screen.blit(text_obj, (x, y))


def draw_background():
    # Pozadí: tmavá barva + neonová mřížka, která ubíhá k horizontu
    global grid_offset
    screen.fill(dark_blue)

    horizon = screen_height // 2
    center_x = screen_width // 2

    # slunce - kruh, který "zapadá" za horizont
    pygame.draw.circle(screen, sun_color, (center_x, horizon - 40), 180)
    # tmavé pruhy přes spodní část slunce (čím níž, tím širší)
    for i in range(6):
        y = horizon - 110 + i * 22
        pygame.draw.rect(screen, dark_blue, (0, y, screen_width, 3 + i * 2))
    # podlaha zakryje spodek slunce
    pygame.draw.rect(screen, dark_blue, (0, horizon, screen_width, screen_height - horizon))

    # svislé čáry - nahoře u horizontu jsou blíž u sebe (perspektiva)
    for x in range(-screen_width, screen_width * 2, 100):
        top_x = center_x + (x - center_x) // 6
        pygame.draw.line(screen, purple, (top_x, horizon), (x, screen_height))

    # vodorovné čáry - posouvají se dolů
    grid_offset = (grid_offset + 1) % 40
    for y in range(horizon + grid_offset, screen_height, 40):
        pygame.draw.line(screen, purple, (0, y), (screen_width, y))

    # zářící čára horizontu
    pygame.draw.line(screen, neon_pink, (0, horizon), (screen_width, horizon), 3)


def draw_button(rect, text, m_pos):
    # Tlačítko: černý obdélník s neonovým okrajem, pod myší změní barvu
    hover = rect.collidepoint(m_pos)
    border_color = neon_cyan if hover else neon_pink
    pygame.draw.rect(screen, black, rect)
    pygame.draw.rect(screen, border_color, rect, 3)
    draw_text(text, rect.centerx, rect.centery, border_color if hover else white, center=True)


def main_menu():
    # Použijeme globální screen, abychom ji mohli přenastavit po návratu ze hry
    global screen

    # Definice tlačítek (stačí jednou, ne v každém snímku)
    btn_start = pygame.Rect(608, 450, 383, 83)
    btn_settings = pygame.Rect(608, 560, 383, 83)
    btn_close = pygame.Rect(608, 670, 383, 83)

    while True:
        m_pos = pygame.mouse.get_pos()

        # Vykreslení
        draw_background()
        draw_text("NEON//GHOST", screen_width // 2, 200, neon_cyan, center=True, use_font=title_font)
        draw_button(btn_start, "START", m_pos)
        draw_button(btn_settings, "SETTINGS", m_pos)
        draw_button(btn_close, "CLOSE", m_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if btn_start.collidepoint(m_pos):
                    start_game()
                    # Po skončení hry vynutíme návrat k rozlišení menu
                    screen = pygame.display.set_mode((screen_width, screen_height))

                if btn_settings.collidepoint(m_pos):
                    settings_menu()

                if btn_close.collidepoint(m_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(60)

def settings_menu():
    running = True
    
def start_game():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # ESC = zpět do menu
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # RENDER YOUR GAME HERE
        draw_text("HRA - ESC zpet do menu", screen_width // 2, screen_height // 2, center=True)

        # flip() zobrazi změny
        pygame.display.flip()

        clock.tick(60)


main_menu()