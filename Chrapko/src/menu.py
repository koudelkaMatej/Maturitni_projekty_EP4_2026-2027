from pathlib import Path
import pygame

# nastavení okna hry
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Flappy Bird")

# Cesta a nacteni obrazku tlacitek
image_folder = Path(__file__).resolve().parent / "obrazky"
start_image = pygame.transform.smoothscale(
    pygame.image.load(image_folder / "start.png").convert_alpha(), (260, 82)
)
exit_image = pygame.transform.smoothscale(
    pygame.image.load(image_folder / "exit.png").convert_alpha(), (260, 89)
)

# Pozice tlacitek a nadpisu plus font pro nadpis
start_button = start_image.get_rect(center=(400, 300))
exit_button = exit_image.get_rect(center=(400, 410))
title_font = pygame.font.SysFont(None, 64)
title = title_font.render("Flappy Bird", True, (255, 255, 255))

# Herni smycka
run = True
while run:
    # Ovladani a ukonceni
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1
              and exit_button.collidepoint(event.pos)):
            run = False

    # Vykresleni na obrazovku(barva pozadi, nadpis a tlacitka)
    screen.fill((0, 0, 0))
    screen.blit(title, title.get_rect(center=(400, 160)))
    screen.blit(start_image, start_button)
    screen.blit(exit_image, exit_button)

    #zobrazí vsechny vykreslene prvky na obrazovku
    pygame.display.flip()

# Ukonceni programu
pygame.quit()
