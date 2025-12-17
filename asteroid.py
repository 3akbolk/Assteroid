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
        
    def split(self):
        
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        elif self.radius > ASTEROID_MIN_RADIUS:
            self.kill()
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(angle)
            velocity2 = self.velocity.rotate(-angle)
            new_radi = self.radius - ASTEROID_MIN_RADIUS
            ass1 = Asteroid(self.position.x, self.position.y, new_radi)
            ass2 = Asteroid(self.position.x, self.position.y, new_radi)
            ass1.velocity = (velocity1 * 1.2)
            ass2.velocity = (velocity2 * 1.2)


            
