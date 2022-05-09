"""
Garden view class. Everything in this file contains elements belonging
to the view portion of the MVC architecture.
"""
import pygame
from model import GardenModel, get_player #Tile, Level, StartScreen, Button, get_player


class GardenView():
    """
    This class contains everything necessary to display the model of the game,
    the view, in a way that is easily understandable by the user.

    Attributes:
        self.surface: A pygame surface on which visuals will be displayed. This
            is passed in when an instance of this class is created.
        self.screen: A pygame surface of width 800 and height 500.
        self.level: An instance of the Level class within the GardenModel class.
        self.player: A global instance of the player class.
        self.button: An instance of the Button class within the GardenModel
            class.
        self.start: An instance of the StartScreen class within the GardenModel
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
        Visualizes the game screen, which includes the background and the
        entire level map.
        """
        self.screen.blit(self.level.background, (0, 0))
        self.level.static_tiles.draw(self.surface)
        points = 0
        # Points display
        pygame.draw.rect(self.surface, (255,248,220), pygame.Rect(10, 460, 125, 50))

        # # Draw points text
        # self.draw_text(f"collected: {points}", 22, (0, 0, 0), (70, 470))
        
        # points = 3 - len(self.level.kill_tiles)
        # # print(self.level.points)

    def draw_player(self):
        """
        Visualizes the player on the screen.
        """
        self.surface.blit(self.player.player, (self.player.rect.centerx, self.player.rect.centery))

    def draw_home(self):
        """
        Visualizes the home screen, which includes the button, title, and
        background.
        """
        self.screen.blit(self.start.screen_surface, (0,0))
        self.screen.blit(self.start.title_surface, self.start.title_rect)
        self.screen.blit(self.button.start_button, self.button.rect)
