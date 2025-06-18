import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius, asteroid_image):
        super().__init__(x,y,radius)
        self.asteroid_image = asteroid_image
        
    def draw(self,screen):
        asteroid_image_scaled = pygame.transform.scale(self.asteroid_image,(self.radius,self.radius))
        screen.blit(asteroid_image_scaled,(self.position.x,self.position.y))
        #pygame.draw.circle(screen,"white",self.position,self.radius,2)
        
    def update(self, dt):
        self.position += (self.velocity*dt)
        
        #added one to avoid problems at spawn
        left_edge = 0 - ASTEROID_MAX_RADIUS - 1
        right_edge = SCREEN_WIDTH + ASTEROID_MAX_RADIUS + 1
        top_edge = 0 - ASTEROID_MAX_RADIUS - 1
        bottom_edge = SCREEN_WIDTH + ASTEROID_MAX_RADIUS + 1
        
        if self.position.x < left_edge or self.position.x > right_edge or self.position.y < top_edge or self.position.y > bottom_edge:
            self.kill()
    
    def split(self, counter):
        self.kill()
        points = 50
        if self.radius <= ASTEROID_MIN_RADIUS:
            counter.update(points)
            return 
        elif self.radius/ASTEROID_MIN_RADIUS == 2:
            points *= 2
            counter.update(points)
        else:
            points *= 3
            counter.update(points)
               
        angle = random.uniform(20,50)
        a1_velocity = self.velocity.rotate(angle)
        a2_velocity = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new1_asteroid = Asteroid(self.position.x,self.position.y,new_radius,self.asteroid_image)
        new2_asteroid = Asteroid(self.position.x,self.position.y,new_radius,self.asteroid_image)
        new1_asteroid.velocity = a1_velocity * ASTEORID_ADDED_VELOCITY
        new2_asteroid.velocity = a2_velocity * ASTEORID_ADDED_VELOCITY