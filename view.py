"""
Garden view class. Everything in this file contains elements belonging
to the view portion of the MVC architecture.
"""
# pylint: disable=protected-access
# we have to access protected member to display it

import pygame
from pygame import mixer
from model import get_player


class GardenView():
    """
    This class contains everything necessary to display the model of the game,
    the view, in a way that is easily understandable by the user.

    Attributes:
        surface: A pygame surface on which visuals will be displayed. This
            is passed in when an instance of this class is created.
        screen: A pygame surface of width 800 and height 500.
        level: An instance of the Level class within the GardenModel class.
        player: A global instance of the player class.
        button: An instance of the Button class within the GardenModel class.
        start: An instance of the StartScreen class within the GardenModel
            class.
    """

    def __init__(self, surface, model):
        """
        Constructs all necessary attributes for the view class.

        Args:
            surface: A pygame surface on which the level map will be displayed.
        """
        self.surface = surface
        self.screen = pygame.display.set_mode((800, 500))
        self.level = model.Level(self.surface)
        self.player = get_player()
        self.button = model.Button()
        self.start = model.StartScreen()

    def draw_game(self):
        """
        Visualizes the game screen, which includes the background, the entire
        level map, and the rectangle background for the point tracking.
        """
        self.screen.blit(self.level.background, (0, 0))
        self.level._static_tiles.draw(self.surface)

        # Points display
        pygame.draw.rect(self.surface, (255, 248, 220),
                         pygame.Rect(10, 460, 125, 50))

    def draw_player(self):
        """
        Visualizes the player on the screen.
        """
        self.surface.blit(self.player.player,
                          (self.player.rect.centerx, self.player.rect.centery))

    def draw_home(self):
        """
        Visualizes the home screen, which includes the button, title, and
        background.
        """
        self.screen.blit(self.start.screen_surface, (0, 0))
        self.screen.blit(self.start.title_surface, self.start.title_rect)
        self.screen.blit(self.button.start_button, self.button.rect)


def music():
    """
    Loads the background music file and plays it on repeat.
    """
    mixer.init()
    mixer.music.load("graphics/background_music.ogg")
    mixer.music.play(-1)
