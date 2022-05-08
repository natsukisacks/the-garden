"""
Garden model class. Everything in this file contains elements belonging
to the model portion of the MVC architecture.
"""
import pygame


class GardenModel():
    """
    This class contains everything necessary to create the model of the game.
    """
    class Player(pygame.sprite.Sprite):
        """
        A class to represent the player sprite and its actions.

        Attributes:
        self.player: The player created by scaling a PNG file to a 64x64 sprite.
        self.rect: A rectangle around the player sprite defined by the player
          sprite.
        self.rect.centerx: An integer representing the player's x position
          relative to the center of the sprite. This integer is the 0th index
          of a tuple passed into the Player class representing the x and y
          positions of the player.
        self.rect.centery: An integer representing the player's y position
          relative to the center of the sprite. This integer is the first index
          of a tuple passed into the Player class representing the x and y
          positions of the player.
        """

        def __init__(self, pos):
            """
            Constructs all necessary attributes for the Player class.

            Args:
            pos: The initial position of the player sprite, passed in as a
              tuple of integers ranging from [0, 800] for the 0th index of this
              argument and [0, 400] for the first index of this argument.
            """
            super().__init__()
            image = pygame.image.load(
                "player_character.png").convert_alpha()
            self.player = pygame.transform.scale(image, (32, 64))
            self.rect = self.player.get_rect(center=pos)

            # Player's initial position
            self.rect.centerx = pos[0]
            self.rect.centery = pos[1]

    class Tile(pygame.sprite.Sprite):
        """
        A class to represent the tiles that make up the game (i.e. all sprites
        not including the player).

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
        self.display_surface: The background surface on which all other visuals
          will be placed.
        player: A global instance of the Player class

        Methods:
        setup_level(layout): Creates the game visuals based on their position in
          the world map in settings.py.
        """

        def __init__(self, surface):
            """
            Constructs all necessary attributes for the Level class.

            Args:
                surface: The surface on which the tiles will be placed.
            """
            self.display_surface = surface
            background = pygame.image.load("background.png")
            self.background = pygame.transform.scale(background, (800, 500))
            self.display_surface = surface
            self.player = get_player()
            self.points = 0
            # WIDTH = 1280
            # HEIGHT = 720
            self.TILESIZE = 32
            self.WORLD_MAP = [
              [" ", "h", "h", "h", "h", "h", "h", "h", "h", "h", "h", "h", "h",\
                "h", "h", "h", "h", "h", "h", "h", "h", "h", "h", "r", " "],
              [" ", "v", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",\
                " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "v", " "],
              [" ", "v", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",\
                " ", " ", " ", " ", "S", " ", " ", " ", " ", " ", "v", " "],
              [" ", "v", " ", " ", " ", " ", " ", " ", "t", " ", " ", " ", " ",\
                " ", " ", " ", " ", " ", " ", "S", " ", " ", " ", "v", " "],
              [" ", "v", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",\
                " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "v", " "],
              [" ", "v", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",\
                " ", "t", " ", " ", " ", " ", " ", " ", " ", " ", "v", " "],
              [" ", "v", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",\
                " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "v", " "],
              [" ", "v", " ", " ", " ", "t", " ", " ", " ", " ", " ", " ", " ",\
                " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "v", " "],
              [" ", "v", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",\
                " ", " ", " ", " ", "S", " ", " ", " ", " ", " ", "v", " "],
              [" ", "v", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",\
                " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "v", " "],
              [" ", "v", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",\
                " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "v", " "],
              [" ", "v", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",\
              " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "v", " "],
              [" ", "v", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",\
                " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "v", " "],
              [" ", "h", "h", "h", "h", "h", "h", "h", "h", "h", "h", "h", "h",\
                "h", "h", "h", "h", "h", "h", "h", "h", "h", "h", "r", " "],
              [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",\
                " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
              ]
            self.setup_level()

        def setup_level(self):
            """
            Places all of the sprite tiles to where they need to be based on
            the world map. Adds these tiles to the appropriate sprite groups.
            """
            self.static_tiles = pygame.sprite.Group()

            # Tiles for the player to collect
            self.kill_tiles = pygame.sprite.Group()

            for row_index, row in enumerate(self.WORLD_MAP):
                for col_index, col in enumerate(row):
                    x_pos = col_index * self.TILESIZE
                    y_pos = row_index * self.TILESIZE

                    if col == "v":
                        self.vert_border = GardenModel.Tile(
                            (x_pos, y_pos), "fence-vertical.png", (16, 40))
                        self.static_tiles.add(self.vert_border)
                    if col == "h":
                        self.hor_border = GardenModel.Tile(
                            (x_pos, y_pos), "fence-horizontal.png", (32, 45))
                        self.static_tiles.add(self.hor_border)
                    if col == "r":
                        self.right_end_border = GardenModel.Tile(
                            (x_pos, y_pos), "fence-right-end.png", (16, 45))
                        self.static_tiles.add(self.right_end_border)
                    if col == "S":
                        self.collect = GardenModel.Tile(
                            (x_pos, y_pos), "tomato.png", (32, 32))
                        self.kill_tiles.add(self.collect)

        # def check_collision(self):
        #     """
        #     Checks if the player is colliding with any tiles in a certain
        #     sprite class and then prevents the player from having free range
        #     around the tile if applicable.
        #     """
        #     for sprite in self.tree_tiles:
        #         if pygame.sprite.collide_rect(self.player, tree):
        #             # moving left
        #             if self.player.rect.left < tree.rect.right:
        #                 self.player.rect.left = tree.rect.right
        #             # moving right
        #             if self.player.rect.right > tree.rect.left:
        #                 self.player.rect.right = tree.rect.left
        #             # moving up
        #             if self.player.rect.top < tree.rect.bottom:
        #                 self.player.rect.top = tree.rect.bottom
        #             # moving down
        #             if self.player.rect.bottom > tree.rect.top:
        #                 self.player.rect.bottom = tree.rect.top

        def kill(self):
          """
          Removes the specified sprite from the sprite list once the player collides with it.
          """
          for collect in self.kill_tiles:
              if pygame.sprite.collide_rect(self.player, collect):
                collect.kill()
                # print(self.kill_tiles)  # the tiles are being removed from the list but are still showing up
                self.points += 1
                print(self.points)
                
        def points(self):
            points = pygame.font.Font("pixel_text.ttf", 40)
            self.points_surface = points.render("Test", False, (115, 79, 150))
            self.points_rect = self.points_surface.get_rect(center=(400, 100))
                
        def update(self):
            """
            Checks if the player is colliding with any tiles.
            """
            # self.check_collision()
            self.kill()

    screen = pygame.display.set_mode((800, 400))

    class StartScreen():
        """
        A class to represent the start screen of the game.

        Attributes:
          self.screen_surface: A screen that serves as a surface to build the
            start screen off of.
          self.title_surface: The surface of the title text.
          self.title_rect: The rectangle around the title text to assist in
            placing the title.
        """

        def __init__(self):
            """
            Constructs all necessary attributes for the Start Screen class.
            """
            # Create a display surface
            self.screen_surface = pygame.Surface((800, 400))
            # Fill entire background with lavender
            self.screen_surface.fill((230, 230, 250))

            # Title
            title = pygame.font.Font("pixel_text.ttf", 40)
            self.title_surface = title.render(
                "Welcome to the Garden!", False, (115, 79, 150))
            self.title_rect = self.title_surface.get_rect(center=(400, 100))

    class Button():
        """
        A class to represent the start button.

        Attributes:
          self.start_button: The start button created by scaling a PNG file
            image.
          self.rect: The rectangle around the start button to help in placing
            it.
          self.clicked: A Boolean attribute that indicates whether the start
            button has been clicked or not.
        """

        def __init__(self):
            """
            Contructs all of the necessary attributes for the Button class.
            """
            start_button = pygame.image.load(
                "start_button.png").convert_alpha()
            self.start_button = pygame.transform.scale(start_button, (130, 64))
            self.rect = self.start_button.get_rect(center=(400, 300))


# Create a global player object to avoid making multiple instances.
player_object = None


def get_player():
    """
    Create a global Player class instance to avoid making multiple instances of
    the same class.

    Returns:
    player_object: An instance of the Player class. If the player_object has not
    already been created, it is created. If it has, the function returns a
    global instance.
    """
    global player_object

    if player_object is None:
        player_object = GardenModel.Player((380, 160))

    return player_object
