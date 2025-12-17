import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
        

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        


    def update(self, delta_time):
        self.position += self.velocity * delta_time
        
    def split():
        old_radi = Asteroid.radius
        spawn_point = Asteroid.position
        if old_radi <= ASTEROID_MIN_RADIUS:
            Asteroid.kill()
            return
        else:
            log_event("asteroid_split")
            old_radi = random.uniform(20, 50)
            Asteroid.velocity.rotate(a)
            Asteroid.velocity.rotate(-a)
            new_radi = old_radi - ASTEROID_MIN_RADIUS
            Asteroid.draw(spawn_point, new_radi)
            Asteroid.draw(spawn_point, new_radi)
            
