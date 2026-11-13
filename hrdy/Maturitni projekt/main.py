import sys
import os
import pygame
import math

pygame.init()

current_dir = os.path.dirname(os.path.abspath(__file__))

# Nastavení okna
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Icy Tower 2.0 - Hlavní menu")

# Barvy
WHITE = (255, 255, 255)
BLUE = (0, 120, 215)
RED = (200, 50, 50)
BLACK = (0, 0, 0)

title_font = pygame.font.SysFont(None, 60)
font = pygame.font.SysFont(None, 40)

# --- NAČTENÍ POZADÍ ---
try:
    image_path = os.path.join(current_dir, "pozadi.png")
    background = pygame.image.load(image_path)
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

except Exception as e:
    print(f"Chyba při načítání: {e}")
    background = None

def draw_text(text, f, color, surface, x, y):
    textobj = f.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    clock = pygame.time.Clock()
    
    while True:
        # --- VYKRESLENÍ POZADÍ ---
        if background:
            screen.blit(background, (0, 0))
        else:
            screen.fill(WHITE)

        # --- POHYBLIVÝ NADPIS SE STÍNEM ---
        tik = pygame.time.get_ticks() * 0.005
        offset_y = math.sin(tik) * 10
        
        # Výpočet pozice, aby byl nadpis hezky uprostřed
        text_x = 160
        text_y = 100
        
        # 1. Černý stín
        draw_text("Icy Tower 2.0", title_font, BLACK, screen, text_x + 3, text_y + int(offset_y) + 3)
        # 2. Hlavní bílý text
        draw_text("Icy Tower 2.0", title_font, WHITE, screen, text_x, text_y + int(offset_y))

        # --- TLAČÍTKA ---
        start_button = pygame.Rect(200, 350, 200, 50)
        exit_button = pygame.Rect(200, 450, 200, 50)

        pygame.draw.rect(screen, BLUE, start_button)
        pygame.draw.rect(screen, RED, exit_button)

        draw_text("SPUSTIT HRU", font, WHITE, screen, 206, 360)
        draw_text("UKONČIT", font, WHITE, screen, 235, 460)

        # --- ZPRACOVÁNÍ UDÁLOSTÍ ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if start_button.collidepoint(pos):
                        print("Spouštím hru...")  
                    if exit_button.collidepoint(pos):
                        pygame.quit()
                        sys.exit()

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main_menu()