import pygame
import constants
import player
from logger import log_state
import asteroid
import asteroidfield


def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    width = constants.SCREEN_WIDTH
    height = constants.SCREEN_HEIGHT
    radius = constants.PLAYER_RADIUS
    asteroid.Asteroid.containers = (asteroids,updatable,drawable)
    player.Player.containers = (updatable,drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    asfield = asteroidfield.AsteroidField()
    game_clock = pygame.time.Clock()
    dt = 0
    tri_player = player.Player(width/2,height/2,radius)
    screen = pygame.display.set_mode((width,height))
    x=0
    y=0
    while x == y:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        updatable.update(dt)
        for i in drawable: 
            i.draw(screen)
        pygame.display.flip()
        dt=game_clock.tick(60)/1000
        

    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}!")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")

if __name__ == "__main__":
    main()
