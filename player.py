import  Circleshape, pygame
from constants import *
from shoot import Shot

class Player(Circleshape.CircleShape):
    def __init__(self, x, y, all_shots=None):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.all_shots = all_shots
        self.shooting_timer = 0
        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        return PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotation -= self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotation += self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        
        if self.shooting_timer > 0:
            # If the shooting timer is still active, decrement it
            self.shooting_timer -= dt
            if self.shooting_timer < 0:
                self.shooting_timer = 0
        
        if keys[pygame.K_SPACE] and self.shooting_timer <= 0 :
            self.shoot(dt)
            self.shooting_timer = PLAYER_SHOOT_COOLDOWN

        
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def shoot(self, dt):
        velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        shot = Shot(self.position.x, self.position.y, velocity)