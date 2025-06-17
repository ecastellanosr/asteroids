import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shots import Shot
from points import Points_counter

def main():
    pygame.init()
    
    pygame.display.set_caption("Asteroids")
    # pygame.display.set_icon()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    #delta time and point initiation
    dt = 0 
    points_counter = 0
    
    #groups for each functionality and drawings
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    #adding objects to the groups
    Shot.containers = (shots,updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable,drawable)
    Points_counter.containers = (drawable)
    #Player initiation as ship
    player = Player((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2))
    counter = Points_counter(COUNTER_X,COUNTER_Y,
                             COUNTER_FONT,COUNTER_SIZE,
                             points_counter)
    
    #asteroid field for all screen and asteroid generation
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

        
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split(counter)
                    shot.kill()
                    
                    
        
        screen.fill("black")
        for drawing in drawable:
            drawing.draw(screen)

        pygame.display.flip()
        #limit framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
