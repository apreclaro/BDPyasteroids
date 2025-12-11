import pygame
import constants
import player
import logger
import asteroid
import asteroidfield
import sys
import shot


def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    width = constants.SCREEN_WIDTH
    height = constants.SCREEN_HEIGHT
    radius = constants.PLAYER_RADIUS
    asteroid.Asteroid.containers = (asteroids,updatable,drawable)
    player.Player.containers = (updatable,drawable)
    shot.Shot.containers = (shots,updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    asfield = asteroidfield.AsteroidField()
    shoots = shot.Shot 
    game_clock = pygame.time.Clock()
    dt = 0
    tri_player = player.Player(width/2,height/2,radius)
    screen = pygame.display.set_mode((width,height))
    x=0
    y=0
    
    while x == y:
        logger.log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        updatable.update(dt)
        
        for aster in asteroids:
            if tri_player.collides_with(aster):
                logger.log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        for aster in asteroids:
            for bullet in shots:
                if bullet.collides_with(aster):
                    logger.log_event("asteroid_shot")
                    bullet.kill()
                    aster.split()
        for i in drawable: 
            i.draw(screen)
        
        pygame.display.flip()
        dt=game_clock.tick(60)/1000
        

    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}!")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    print(f"Screen width: {constants.SCREEN_WIDTH}")

if __name__ == "__main__":
    main()
