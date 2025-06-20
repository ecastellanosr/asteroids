import pygame
from circleshape import CircleShape
from constants import *
from shots import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shooting_timer = 0
        self.lives = 3
        self.death_timer = 0
        self.blink_timer = 0
    
    def draw(self,screen):
        if self.blink_timer > 0.0:
            pygame.draw.polygon(screen,"black",self.triangle(),2)
        else:
            pygame.draw.polygon(screen,"white",self.triangle(),2)
        #hitbox
        #pygame.draw.circle(screen,"white",self.position,self.radius,2)

        
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self,dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
    
    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * (PLAYER_SPEED * dt)
        
     
    def update(self, dt):
        self.shooting_timer -= dt
        self.death_timer -= dt
        self.blink_timer -= dt
        if self.death_timer > 0 and self.blink_timer < -PLAYER_BLINK_COOLDOWN:
            self.blink_timer = PLAYER_BLINK_COOLDOWN
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.shooting_timer > 0:
            return
        shot = Shot(self.position.x,self.position.y,self.rotation)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.shooting_timer = PLAYER_SHOOT_COOLDOWN
        
    def collided(self):
        if self.death_timer > 0:
            return 
        self.death_timer = PLAYER_DEATH_COOLDOWN
        self.blink_timer = PLAYER_BLINK_COOLDOWN
    
    def restart(self):
        self.position = pygame.Vector2((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2)).rotate(0)
        self.rotation = 0
        self.shooting_timer = 0
        self.lives = 3
        self.death_timer = 0
         