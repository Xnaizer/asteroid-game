import pygame
import constants
from logger import log_state

def main():
    print(f"[GAME] Starting Asteroids with pygame version: {pygame.version.ver}")
    print("[GAME] Starting Asteroids...")
    print(f"[GAME] Screen width: {constants.SCREEN_WIDTH}")
    print(f"[GAME] Screen height: {constants.SCREEN_HEIGHT}")

    pygame.init()
    
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))    

    clock_time = pygame.time.Clock()
    dt = 0
    
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("[GAME] Shutting down..")
                return

        screen.fill("black")

        pygame.display.flip()

        tick_time = clock_time.tick(60)
        dt = tick_time / 1000
        # print(dt)

if __name__ == "__main__":
    main()

