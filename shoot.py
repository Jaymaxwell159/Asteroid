import pygame
from Circleshape import CircleShape
from constants import *


class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.color = "yellow"
        self.velocity = pygame.Vector2(velocity)
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, width=0)

    def update(self, dt):
        self.position += self.velocity * dt