import pygame
import random
from Circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = int(radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        """Split the asteroid into two smaller asteroids."""
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            random_angle = random.uniform(20, 50)
            a = self.velocity.rotate(random_angle)
            b = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_a.velocity = a*1.2
            asteroid_b.velocity = b*1.2
            asteroid_a.add(self.containers)
            asteroid_b.add(self.containers)
            return asteroid_a, asteroid_b