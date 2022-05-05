import pygame, sys
from player import Player, get_player
from home_screen import StartScreen, Button
from settings import *
from model import Level, Tile

# Display setup
pygame.init()
screen = pygame.display.set_mode((800, 400))

# player = Player((400, 200)) # create an instance
player = get_player()
start_screen = StartScreen()
button = Button()
clock = pygame.time.Clock()
level = Level(WORLD_MAP, screen)
tile = Tile((400, 200))

while True:
    # handle every event since the last frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit the screen
            sys.exit()

    # if button.clicked == True:
    screen.fill((144, 238, 144))
    player.handle_keys() # handle_keys() isn't working with the player using level.run()
        # figure it out later -- for now, use the reg. player draw method to move it around and
        # test collisions
    level.run() # draws the map
      # take out player from map
    player.check_collision_x(tile.rect)
    player.draw(screen)

    # Display the home screen
    # if button.clicked == False:
    #   player.handle_keys() # handle the keys
    #   start_screen.draw()
    #   button.draw(screen)
    #   player.draw(screen) # draw the player to the screen

    pygame.display.update()
    
    clock.tick(60)