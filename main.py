import pygame
import constants
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys

def main():
    print(f"[GAME] Starting Asteroids with pygame version: {pygame.version.ver}")
    print("[GAME] Starting Asteroids...")
    print(f"[GAME] Screen width: {constants.SCREEN_WIDTH}")
    print(f"[GAME] Screen height: {constants.SCREEN_HEIGHT}")

    pygame.init()
    
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))    

    clock_time = pygame.time.Clock()
    dt = 0

    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2 

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroid_field = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (asteroid_field, updatable)
    
    player_data = Player(x,y)
    asteroid_field_data = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("[GAME] Shutting down..")
                return

        screen.fill("black")
        
        updatable.update(dt)

        for thing in asteroids:
           if thing.collides_with(player_data):
               log_event("player_hit")
               print("[GAME] Game over !")
               sys.exit()

        for thing in drawable:
            thing.draw(screen)
        
        pygame.display.flip()
        
        dt = clock_time.tick(60) / 1000
        print(dt)

if __name__ == "__main__":
    main()

