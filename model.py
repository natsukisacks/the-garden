""" Creates the map that everything is based upon. """
import pygame
from settings import *
# from player import Player, get_player


class GardenModel():
    class Player(pygame.sprite.Sprite):
        """
        A class to represent the player sprite and its actions.

        Attributes:
        self.player: The player created by scaling a PNG file to a 64x64 sprite.
        self.rect: A rectangle around the player sprite defined by the player sprite.
        self.x: An integer representing the player's x position. This integer is the 0th index
            of a tuple passed into the Player class representing the x and y positions of the player.
        self.y: An integer representing the player's y position. This integer is the first index
            of a tuple passed into the Player class representing the x and y positions of the player.
        """

        def __init__(self, pos):
            """
            Constructs all necessary attributes for the Player class.

            Args:
            pos: The initial position of the player sprite, passed in as a tuple of integers
                ranging from [0, 800] for the 0th index of this argument and [0, 400] for the
                first index of this argument.
            """
            super().__init__()
            image = pygame.image.load(
                "graphics/player_character.png").convert_alpha()
            self.player = pygame.transform.scale(image, (32, 64))
            self.rect = self.player.get_rect(center=pos)

            # Player's initial position
            self.rect.centerx = pos[0]
            self.rect.centery = pos[1]

            # self.rect = pygame.Rect.move(self.rect, self.x - x_old, self.y - y_old)

    class Tile(pygame.sprite.Sprite):
        """
        A class to represent the tiles that make up the game (i.e. all sprites not including the player).

        Attributes:
        image: An image representing the tile. A scaled PNG image.
        rect: The rectangle around the tile image.
        player: A global instance of the player class.
        """

        def __init__(self, pos, filename, scale):
            """
            Constructs all necessary attributes for the Tile class.
            """
            # Initiating the parent Sprite class
            super().__init__()
            image = pygame.image.load(filename).convert_alpha()
            self.image = pygame.transform.scale(image, scale)
            self.rect = self.image.get_rect(topleft=pos)
            self.player = get_player()

    class Level():
        """
        A class to represent the actual game display itself.

        Attributes:
        display_surface: The background surface on which all other visuals will be placed.
        player: A global instance of the Player class

        Methods:
        setup_level(layout): Creates the game visuals based on their position in the world map
            in settings.py.
        """

        def __init__(self, level_map, surface):
            """
            Constructs all necessary attributes for the Level class.

            Args:
                level_map: The world map as seen in settings.py. It represents where everything should go.
                It is a list of lists of strings.
                surface: The surface on which the tiles will be placed.
            """
            self.display_surface = surface
            self.setup_level(level_map)
            self.player = get_player()
            background = pygame.image.load("graphics/background-test.png")
            self.background = pygame.transform.scale(background, (800, 500))
            self.display_surface = surface
            self.setup_level(level_map)
            self.player = get_player()

        def setup_level(self, level_map):
            """
            Utilizes the world map in settings.py to place all tiles where they need to be.

            Args:
                layout: The layout of the tiles.
            """
            self.all_tiles = pygame.sprite.Group()
            self.tree_tiles = pygame.sprite.Group()

            for row_index, row in enumerate(level_map):
                for col_index, col in enumerate(row):
                    x = col_index * TILESIZE
                    y = row_index * TILESIZE

                    if col == "v":
                        self.vert_border = GardenModel.Tile(
                            (x, y), "graphics/fence-vertical.png", (16, 40))
                        self.all_tiles.add(self.vert_border)
                    if col == "h":
                        self.hor_border = GardenModel.Tile(
                            (x, y), "graphics/fence-horizontal.png", (32, 45))
                        self.all_tiles.add(self.hor_border)
                    if col == "r":
                        self.right_end_border = GardenModel.Tile(
                            (x, y), "graphics/fence-right-end.png", (16, 45))
                        self.all_tiles.add(self.right_end_border)
                    if col == "T":
                        self.tree = GardenModel.Tile(
                            (x, y), "graphics/mantis_shrimp.webp", (90, 90))
                        self.tree_tiles.add(self.tree)
                        self.all_tiles.add(self.tree)

        def check_collision(self):
            # gets rid of trees as you go near them
            # for tree in self.tree_tiles:
            #   if pygame.sprite.collide_rect(self.player, tree):
            #     tree.kill()
            for tree in self.tree_tiles:
                if pygame.sprite.collide_rect(self.player, tree):
                    if self.player.rect.left < tree.rect.right:  # player is moving left
                        self.player.rect.left = tree.rect.right
                    if self.player.rect.right > tree.rect.left:
                        self.player.rect.right = tree.rect.left
                    if self.player.rect.top < tree.rect.bottom:
                        self.player.rect.top = tree.rect.bottom
                    if self.player.rect.bottom > tree.rect.top:
                        self.player.rect.bottom = tree.rect.top

        def update(self):
            """
            Displays the game surface with the tiles and calls the screen scrolling function.
            """
            self.check_collision()

    screen = pygame.display.set_mode((800, 500))

    class StartScreen():
        """
        A class to represent the start screen of the game.

        Attributes:
          self.screen_surface: A screen that serves as a surface to build the start screen off of.
          self.title_surface: The surface of the title text.
          self.title_rect: The rectangle around the title text to assist in placing the title.
        """

        def __init__(self):
            """
            Constructs all necessary attributes for the Start Screen class.
            """
            # Create a display surface
            self.screen_surface = pygame.Surface((800, 500))
            # Fill entire background with lavender
            self.screen_surface.fill((230, 230, 250))

            # Title
            title = pygame.font.Font("graphics/pixel_text.ttf", 40)
            self.title_surface = title.render(
                "Welcome to the Garden!", False, (115, 79, 150))
            self.title_rect = self.title_surface.get_rect(center=(400, 100))

    class Button():
        """
        A class to represent the start button.

        Attributes:
          self.start_button: The start button created by scaling a PNG file image.
          self.rect: The rectangle around the start button to help in placing it.
          self.clicked: A Boolean attribute that indicates whether the start button has been
            clicked or not.
        """

        def __init__(self):
            """
            Contructs all of the necessary attributes for the Button class.
            """
            start_button = pygame.image.load(
                "graphics/start_button.png").convert_alpha()
            self.start_button = pygame.transform.scale(start_button, (130, 64))
            self.rect = self.start_button.get_rect(center=(400, 300))


# Create a global player object to avoid making multiple instances.
player_object = None


def get_player():
    """ 
    Create a global Player class instance to avoid making multiple instances of the same class.

    Returns:
    player_object: An instance of the Player class. If the player_object has not
    already been created, it is created. If it has, the function returns a global instance.
    """
    global player_object

    if player_object is None:
        player_object = GardenModel.Player((380, 160))

    return player_object
