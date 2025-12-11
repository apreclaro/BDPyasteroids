import circleshape
import pygame
import constants
import logger
import random

class Asteroid(circleshape.CircleShape):
    
    def __init__ (self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        color = "white" 
        pygame.draw.circle(screen, color, self.position, self.radius, constants.LINE_WIDTH)
    
    def update(self,dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            logger.log_event("asteroid_split")
            angle = random.uniform(20,50)
            first = self.velocity.rotate(angle)
            second = self.velocity.rotate(-angle)
            new_radii = self.radius - constants.ASTEROID_MIN_RADIUS
            asone = Asteroid(self.position.x,self.position.y,new_radii)
            astwo = Asteroid(self.position.x,self.position.y,new_radii)
            asone.velocity = first * 1.2
            astwo.velocity = second * 1.2