import pygame, sys
from settings import *
from level import Level
# from model import title_screen

class Game:
    def __init__(self):
        # General set up
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("The Garden")
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Create the title screen
                # title_screen(screen)

                # Display the screen
                self.screen.fill("black")
                self.level.run()
                pygame.display.update()
                self.clock.tick(FPS)  # updating the image 60x/sec

if __name__ == "__main__":
    game = Game()
    game.run()