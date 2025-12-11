import pygame
import constants
from logger import log_state


def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    x=0
    y=0
    while x == y:
        log_state()
        screen.fill("black")
        pygame.display.flip()

    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}!")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")

if __name__ == "__main__":
    main()
