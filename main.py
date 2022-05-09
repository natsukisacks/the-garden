"""
Calls of the class and method instances necessary to properly display the
interactive game.
"""
import sys
import pygame
from model import GardenModel, get_player
from view import GardenView
from controller import GardenController
from pygame import mixer

mixer.init()

# Display setup
pygame.init()
screen = pygame.display.set_mode((800, 500))  # , pygame.FULLSCREEN)

model = GardenModel()
player = get_player()
start_screen = model.StartScreen()
button = model.Button()
clock = pygame.time.Clock()
level = model.Level(screen)
view = GardenView(screen, model)
controller = GardenController(model)

mixer.music.load("graphics/background_music.ogg")
mixer.music.play(-1)

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
        level.update()  # draws the map

    # Display the home screen
    if controller.clicked is False:
        controller.handle_keys()  # handle the keys
        view.draw_home()
        controller.update_button()
        view.draw_player()

    pygame.display.update()

    clock.tick(60)
