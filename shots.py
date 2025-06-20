import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self,x,y,rotation):
        super().__init__(x,y,SHOT_RADIUS)
        self.rotation = rotation
        
    def draw(self,screen):
        #pygame.draw.circle(screen,"white",self.position,self.radius,2)
        pygame.draw.polygon(screen,"white",self.rectangle())
        
    # in the player class
    def rectangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius - right
        b = self.position + forward * self.radius + right
        c = self.position - forward * self.radius + right 
        d = self.position - forward * self.radius - right
        
        return [a,b,c,d]
        
    def update(self, dt):
        self.position += (self.velocity*dt)
        
        left_edge = 0 - ASTEROID_MAX_RADIUS - 1
        right_edge = SCREEN_WIDTH + ASTEROID_MAX_RADIUS + 1
        top_edge = 0 - ASTEROID_MAX_RADIUS - 1
        bottom_edge = SCREEN_WIDTH + ASTEROID_MAX_RADIUS + 1
        
        if self.position.x < left_edge or self.position.x > right_edge or self.position.y < top_edge or self.position.y > bottom_edge:
            self.kill()
     