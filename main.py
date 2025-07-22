import asyncio
import pygame
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shoot import Shot

async def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    game_clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    all_asteroids = pygame.sprite.Group()

    all_shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    
    Asteroid.containers = (updatable, drawable, all_asteroids)
    
    AsteroidField.containers = (updatable,)

    Shot.containers = (updatable, drawable, all_shots)
    
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2, all_shots=all_shots)
    
    asteroid_field = AsteroidField()
    print("Starting Asteroids! \n"
    f"Screen width: {SCREEN_WIDTH} \n"
    f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in all_asteroids:
            if asteroid.collide(player):
                print("Game over !")
                # Handle collision (e.g., end game, reduce health, etc.)
                return;
            for shot in all_shots:
                if asteroid.collide(shot):
                    asteroid.split()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()
            
        dt = game_clock.tick(60) / 1000.0
        await asyncio.sleep(0)


if __name__ == "__main__":
    asyncio.run(main())
