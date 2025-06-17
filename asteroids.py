import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
        
    def update(self, dt):
        self.position += (self.velocity*dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        a1_velocity = self.velocity.rotate(angle)
        a2_velocity = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new1_asteroid = Asteroid(self.position.x,self.position.y,new_radius)
        new2_asteroid = Asteroid(self.position.x,self.position.y,new_radius)
        new1_asteroid.velocity = a1_velocity * ASTEORID_ADDED_VELOCITY
        new2_asteroid.velocity = a2_velocity * ASTEORID_ADDED_VELOCITY