import constants
import circleshape
import pygame
import shot

class Player(circleshape.CircleShape):
    
    def __init__(self, x, y, z):
        super().__init__(x,y,z)
        self.rotation = 0
        self.fired = 0
        self.limiter = 0
        
        

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        color = "white" 
        points = self.triangle()
        width = constants.LINE_WIDTH
        pygame.draw.polygon(screen, color, points, width)

    def rotate(self,dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt
    
    def update(self,dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
            
        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)
            
        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_SPACE]:
            if self.limiter > 0:
                return
            else:
                self.shoot()
                self.limiter = constants.PLAYER_SHOOT_COOLDOWN_SECONDS

        self.limiter -= dt
    
    def move(self,dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * constants.PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
    
    def shoot(self):
        bullet = shot.Shot(self.position.x, self.position.y)
       
        bullet.velocity = pygame.Vector2(0,1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED