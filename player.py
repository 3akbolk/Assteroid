import pygame
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape, pygame. sprite. Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        color = "white"
        points = self.triangle()
        line = LINE_WIDTH
        pygame.draw.polygon(screen, color, points, line)

    def rotate(self, delta_time):
        self.rotation += (PLAYER_TURN_SPEED * delta_time) 

    def move(self, delta_time):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * delta_time
        self.position += rotated_with_speed_vector

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)

        pewpew = pygame.Vector2(0, 1)
        direction = pewpew.rotate(self.rotation)
        shot.velocity = direction * PLAYER_SHOOT_SPEED
        



    def update(self, delta_time):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-delta_time)

        if keys[pygame.K_d]:
            self.rotate(delta_time)

        if keys[pygame.K_w]:
            self.move(delta_time)
            
        if keys[pygame.K_s]:
            self.move(-delta_time)

        if keys[pygame.K_SPACE]:
            self.shoot()

    