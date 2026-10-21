import pygame
from enemy import Enemy

# Initialize Pygame
pygame.init()

#clock
clock = pygame.time.Clock()

#Základní nastavení proměnných
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60


# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Moje hra")

#load images
enemy_image = pygame.image.load("Projekt/Hra/assets/images/zombie1.png").convert_alpha()

#crate groups
enemy_group = pygame.sprite.Group()


waypoints = [(100, 200), (200, 100), (300, 500), (400, 100), (200, 300), (100, 300), (700, 600)]

enemy= Enemy(waypoints, enemy_image)
enemy_group.add(enemy)

# Main game loop
running = True
while running:

    clock.tick(FPS)  # Limit FPS

    screen.fill("grey32")

    #draw enemy path
    pygame.draw.lines(screen, "grey0", False, waypoints, 5)

    #update groups
    enemy_group.update()


    #draw groups
    enemy_group.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #update the display
    pygame.display.flip()

pygame.quit()