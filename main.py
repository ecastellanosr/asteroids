import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shots import Shot
from points import Points_counter

def main():
    pygame.init()
    game_state = True
    
    pygame.display.set_caption("Asteroids")
    # pygame.display.set_icon()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    #delta time
    dt = 0 
    
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
                             0)
    
    asteroid_images_list = []
    for image in ASTEROID_IMAGES:
        asteroid_image = pygame.image.load(ASTEROID_IMAGES_FOLDER+image).convert_alpha()
        asteroid_images_list.append(asteroid_image)
    
    #asteroid field for all screen and asteroid generation
    asteroid_field = AsteroidField(asteroid_images_list)
    
    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_state = True
                    for asteroid in asteroids:
                        asteroid.kill()
                    player.restart()
                    counter.points = 0
                    
        
        screen.fill("blue")
        
        if game_state == True :
            screen.fill("black")
            updatable.update(dt)
            
            for asteroid in asteroids:
                if asteroid.check_collision(player):
                    if not player.death_timer > 0:
                        print("lost a life")
                        player.lives -= 1
                        player.collided()
                    
                    if player.lives == 0:
                        print("Game over!")
                        game_state = False
                    else:
                        player.just_colidded = True 
            
                for shot in shots:
                    if asteroid.check_collision(shot):
                        asteroid.split(counter)
                        shot.kill()
            
            for drawing in drawable:
                drawing.draw(screen)

        pygame.display.flip()
        #limit framerate to 60 FPS
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()
