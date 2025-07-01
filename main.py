import pygame, constants

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    while True:
        pygame.Surface.fill(screen ,(0, 0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    print("Starting Asteroids! \n"
          f"Screen width: {constants.SCREEN_WIDTH} \n"
          f"Screen height: {constants.SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
