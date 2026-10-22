import pygame
from menu import Menu
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
menu = Menu(screen)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        menu.handle_event(event)
    menu.update()
    menu.draw()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()