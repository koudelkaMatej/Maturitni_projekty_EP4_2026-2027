
import pygame
import sys

pygame.init()

# Nastavení okna
WIDTH = 600
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Had - Main Menu")

# Barvy
BLACK = (20, 20, 20)
GREEN = (50, 220, 100)
WHITE = (255, 255, 255)
DARK_GREEN = (30, 150, 70)
GRAY = (80, 80, 80)

# Fonty
title_font = pygame.font.Font(None, 80)
button_font = pygame.font.Font(None, 45)

# Tlačítka
start_button = pygame.Rect(200, 240, 200, 60)
quit_button = pygame.Rect(200, 330, 200, 60)

clock = pygame.time.Clock()


def draw_button(rect, text, mouse_pos):
    color = DARK_GREEN if rect.collidepoint(mouse_pos) else GRAY

    pygame.draw.rect(screen, color, rect, border_radius=10)

    text_surface = button_font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)

    screen.blit(text_surface, text_rect)


def main_menu():
    while True:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if start_button.collidepoint(event.pos):
                        return "start"

                    if quit_button.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

        # Pozadí
        screen.fill(BLACK)

        # Název hry
        title = title_font.render("HAD", True, GREEN)
        title_rect = title.get_rect(center=(WIDTH // 2, 130))
        screen.blit(title, title_rect)

        # Podtitul
        subtitle = button_font.render("Main Menu", True, WHITE)
        subtitle_rect = subtitle.get_rect(center=(WIDTH // 2, 190))
        screen.blit(subtitle, subtitle_rect)

        # Tlačítka
        draw_button(start_button, "START", mouse_pos)
        draw_button(quit_button, "KONEC", mouse_pos)

        pygame.display.flip()
        clock.tick(60)


def game():
    # Zde později bude samotná hra
    screen.fill(BLACK)

    text = button_font.render("Tady bude hra", True, GREEN)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False


# Spuštění programu
while True:
    choice = main_menu()

    if choice == "start":
        game()
