import sys
import pygame
from constants import *
from logger import log_state, log_event
from player import *
from asteroid import *
from asteroidfield import *
from shot import Shot



def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
          
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    clock = pygame.time.Clock()
    delta_time = 0.1


    #CREATING GROUPS
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = updatable, drawable
    Asteroid.containers = asteroids, updatable, drawable
    AsteroidField.containers = updatable
    Shot.containers = shots

    #CREATING SCREEN SIZE
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)
    assteroids = AsteroidField()
    

    #GAME LOOP START
    while running:
        log_state()
        x += 50 * delta_time

        #ABILITY TO TURN OFF
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        screen.fill("black")


        #ANYTHING THAT CAN UPDATE - UPDATES
        updatable.update(delta_time)


        #ANYTHING THAT CAN DRAW GETS DRAWN
        for players in drawable:
            players.draw(screen)

        #SHOTS UPDATE
        shots.update(delta_time)
        for shot in shots:
            shot.draw(screen)

        for ass in asteroids:
            if player.collides_with(ass):
                log_event("player_hit")
                print("Game over!")
                sys.exit()


        #PROJECT IT TO SCREEN
        pygame.display.flip()
        #TRACK THE DELTA TIME
        delta_time = clock.tick(60) / 1000
        delta_time = max(0.001, min(0.1, delta_time))
        



if __name__ == "__main__":
    main()