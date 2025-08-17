import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        angle_pos = self.velocity.rotate(random_angle)
        angle_neg = self.velocity.rotate(-random_angle)
        self.radius -= ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position[0], self.position[1], self.radius)
        asteroid2 = Asteroid(self.position[0], self.position[1], self.radius)
        asteroid1.velocity = angle_pos * 1.2
        asteroid2.velocity = angle_neg * 1.2
