import pygame
from pygame.math import Vector2

class Enemy(pygame.sprite.Sprite):
    def __init__(self, waypoints, image):
        pygame.sprite.Sprite.__init__(self)
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])  # Start at the first waypoint
        self.target_waypoint = 1
        self.speed = 2
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        self.move()


    def move(self):
        #define  target waypoint
        self.target = Vector2(self.waypoints[self.target_waypoint])
        self.movement = self.target - self.pos

        #calculate distance to target waypoint
        distance = self.movement.length()
        #check if remaining distance is greater than enemy speed
        if distance > self.speed:
            #move enemy towards target waypoint
            self.pos += self.movement.normalize() * self.speed
        else:
            #move enemy to target waypoint and update to next waypoint
            self.pos += self.movement.normalize() * distance
            self.target_waypoint += 1
          

        self.rect.center = self.pos

