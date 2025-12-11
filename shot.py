import circleshape
import pygame
import constants

class Shot(circleshape.CircleShape):
    
    def __init__ (self,x,y):
        
        super().__init__(x,y,constants.SHOT_RADIUS)

    def draw(self, screen):
        color = "white" 
        pygame.draw.circle(screen, color, self.position, self.radius, constants.LINE_WIDTH)
        pass
    
    def update(self, dt):
        self.position += (self.velocity * dt)
        pass