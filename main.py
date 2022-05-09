"""
Calls of the class and method instances necessary to properly display the
interactive game.
"""
import sys
import pygame
from model import GardenModel
from view import GardenView, music
from controller import GardenController

# Display setup
pygame.init()
screen = pygame.display.set_mode((800, 500))

# Create instances of various classes
model = GardenModel()  # to use in instances of GardenModel subclasses
start_screen = model.StartScreen()
button = model.Button()
clock = pygame.time.Clock()
level = model.Level(screen)
view = GardenView(screen, model)
controller = GardenController(model)

# Our background music
music()

while True:
    # handle every event since the last frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # quit the screen
            sys.exit()

    if controller.clicked:
        controller.handle_keys()
        view.draw_game()
        view.draw_player()
        level.update()  # checks for collisions

    # Display the home screen
    if controller.clicked is False:
        controller.handle_keys()
        view.draw_home()
        controller.update_button()
        view.draw_player()

    pygame.display.update()

    clock.tick(60)
