"""
Garden model class. Everything in this file contains elements belonging
to the model portion of the MVC architecture.
"""
import pygame
from pygame import mixer
mixer.init()


class GardenModel():
    """
    This class contains everything necessary to create the model of the game.
    """
    class Player(pygame.sprite.Sprite):
        """
        A class to represent the player sprite and its actions.

        Attributes:
        player: The player created by scaling a PNG file to a 64x64 sprite.
        rect: A rectangle around the player sprite defined by the player
          sprite.
        rect.centerx: An integer representing the player's x position
          relative to the center of the sprite. This integer is the 0th index
          of a tuple passed into the Player class representing the x and y
          positions of the player.
        rect.centery: An integer representing the player's y position
          relative to the center of the sprite. This integer is the first index
          of a tuple passed into the Player class representing the x and y
          positions of the player.
        """

        def __init__(self, pos):
            """
            Constructs all necessary attributes for the Player class.

            Args:
              pos: The initial position of the player sprite, passed in as a
                tuple of integers ranging from [0, 800] for the 0th index of
                this argument and [0, 400] for the first index of this argument.
            """
            super().__init__()
            image = pygame.image.load(
                "graphics/player_character.png").convert_alpha()
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

            Args:
              pos: The initial position of the player sprite, passed in as a
                tuple of integers ranging from [0, 800] for the 0th index of
                this argument and [0, 400] for the first index of this argument.
              filename: A string representing the image to load and scale.
              scale: A tuple of integers representing the width and height to
                scale the image by.

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
        display_surface: The background surface on which all other visuals
          will be placed.
        background: The image scaled for the background.
        player: A global instance of the Player class.
        points: An integer representing the number of produce that the player
          has collected so far.
        win_screen: An instance of the final winning screen. This is a class
          inside of the GardenModel class.
        tilesize: An integer representing the size to scale the tiles by.
        gameover: A boolean representing whether the player has won or not.
        world_map: A list of lists of strings that represents where each sprite
          will go when the sprite group is created.
        """

        def __init__(self, surface):
            """
            Constructs all necessary attributes for the Level class.

            Args:
                surface: A pygame surface representing the surface on which the
                  tiles will be placed.
            """
            self.display_surface = surface
            background = pygame.image.load("graphics/background-7.png")
            self.background = pygame.transform.scale(background, (800, 500))
            self.player = get_player()
            self.points = 0
            self.tilesize = 32
            self.gameover = False
            self.world_map = [
                [" ", "h", "h", "h", "h", "h", "h", "h", "h", "h", "h", "h",
                 "h", "h", "h", "h", "h", "h", "h", "h", "h", "h", "h", "r",
                 " "],
                [" ", "v", " ", " ", " ", " ", " ", "P", " ", " ", " ", " ",
                 " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "v",
                    " "],
                [" ", "v", " ", " ", "c", "p", " ", "c", " ", " ", " ", " ",
                 " ", " ", "T", " ", "T", " ", "T", " ", "T", " ", " ", "v",
                 " "],
                [" ", "v", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                 " ", " ", " ", "T", " ", "T", " ", "T", " ", " ", " ", "v",
                    " "],
                [" ", "v", " ", " ", "c", "p", " ", "c", " ", " ", " ", " ",
                 " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "v",
                    " "],
                [" ", "v", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                 " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "v",
                    " "],
                [" ", "v", " ", " ", "c", "p", " ", "c", " ", " ", " ", " ",
                 " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "v",
                    " "],
                [" ", "v", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                 " ", " ", " ", " ", " ", " ", " ", "t", "p", "t", " ", "v",
                    " "],
                [" ", "v", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                 " ", "s", " ", "s", " ", "s", " ", "t", "p", "t", " ", "v",
                    " "],
                [" ", "v", " ", "w", " ", "w", " ", "w", " ", " ", " ", " ",
                 " ", "s", " ", "s", " ", "s", " ", "t", "p", "t", " ", "v",
                    " "],
                [" ", "v", "w", " ", "w", " ", "w", " ", " ", " ", " ", " ",
                 " ", "s", " ", "s", " ", "s", " ", "t", "p", "t", " ", "v",
                    " "],
                [" ", "v", " ", "w", " ", "w", " ", "w", " ", " ", " ", " ",
                 " ", "s", " ", "s", " ", "s", " ", "t", "p", "t", " ", "v",
                    " "],
                [" ", "v", "w", " ", "w", " ", "w", " ", " ", " ", " ", " ",
                 " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "v",
                    " "],
                [" ", "h", "h", "h", "h", "h", "h", "h", "h", "h", "h", "h",
                 "h", "h", "h", "h", "h", "h", "h", "h", "h", "h", "h", "r",
                    " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                 " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
                    " "],
            ]
            self.setup_level()

        def setup_level(self):
            """
            Places all of the sprite tiles to where they need to be based on
            the world map. Adds these tiles to the appropriate sprite groups.
            """
            # Tiles that don't change throughout the game
            self.static_tiles = pygame.sprite.Group()

            # Tiles for the player to collect
            self.veggie_tiles = pygame.sprite.Group()

            # Create the placement of the world map
            for row_index, row in enumerate(self.world_map):
                for col_index, col in enumerate(row):
                    x_pos = col_index * self.tilesize
                    y_pos = row_index * self.tilesize

                    # Instantiating all of the sprites to their positions
                    if col == "v":
                        self.vert_border = GardenModel.Tile(
                            (x_pos, y_pos), "graphics/fence-vertical.png",\
                              (16, 40))
                        self.static_tiles.add(self.vert_border)
                    if col == "h":
                        self.hor_border = GardenModel.Tile(
                            (x_pos, y_pos), "graphics/fence-horizontal.png",\
                              (32, 45))
                        self.static_tiles.add(self.hor_border)
                    if col == "r":
                        self.right_end_border = GardenModel.Tile(
                            (x_pos, y_pos), "graphics/fence-right-end.png",\
                              (16, 45))
                        self.static_tiles.add(self.right_end_border)
                    if col == "P":
                        self.pom_tree = GardenModel.Tile(
                            (x_pos, y_pos), "graphics/pom_tree.png", (200, 200))
                        self.static_tiles.add(self.pom_tree)
                    if col == "p":
                        self.peas = GardenModel.Tile(
                            (x_pos, y_pos), "graphics/peas.png", (32, 32))
                        self.veggie_tiles.add(self.peas)
                    if col == "w":
                        self.watermelon = GardenModel.Tile(
                            (x_pos, y_pos), "graphics/watermelon.png", (32, 32))
                        self.veggie_tiles.add(self.watermelon)
                    if col == "t":
                        self.potato = GardenModel.Tile(
                            (x_pos, y_pos), "graphics/potato.png", (32, 16))
                        self.veggie_tiles.add(self.potato)
                    if col == "s":
                        self.spotato = GardenModel.Tile(
                            (x_pos, y_pos), "graphics/sweet potato.png",\
                              (32, 16))
                        self.veggie_tiles.add(self.spotato)
                    if col == "T":
                        self.tomato = GardenModel.Tile(
                            (x_pos, y_pos), "graphics/tomato.png", (25, 25))
                        self.veggie_tiles.add(self.tomato)
                    if col == "c":
                        self.collect = GardenModel.Tile(
                            (x_pos, y_pos), "graphics/carrot.png", (16, 45))
                        self.veggie_tiles.add(self.collect)

        def draw_text(self, text, font_size, color, coords):
            """
            Helper function used for drawing text.
            Args:
                text: A string representing the text to draw.
                font_size: An integer containing the size of the font to use.
                color: A tuple representing the color of the font in RGB.
                coords: A tuple containing the coordinates of the position of
                  the text on the screen.
            """
            # Set font
            font = pygame.font.Font("graphics/pixel_text.ttf", font_size)

            # Define a surface with the specified text, color, and font
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect()

            # Position and display the text
            text_rect.midtop = coords
            self.display_surface.blit(text_surface, text_rect)

        def delete_produce(self):
            """
            Removes the specified sprite from the sprite list once the player
            collides with it.
            """
            # Drawing the tiles & text to the surface. Couldn't do this in
            # view.py due to issues with the classes in model.py and view.py not
            # syncing correctly.
            self.veggie_tiles.draw(self.display_surface)
            self.draw_text(f"collected: {self.points}", 35, (0, 0, 0),
                           (70, 470))

            # Initializing the sound effect for picking up veggies.
            collected_sound = mixer.Sound("graphics/collected_music.ogg")

            # Check if the player has picked up a veggie. If so, remove it
            # from the screen and add a point.
            for produce in self.veggie_tiles:
                if pygame.sprite.collide_rect(self.player, produce):
                    produce.kill()
                    collected_sound.play()
                    self.points += 1

            # Once the player gets enough produce, they win!
            if self.points > 20:
                # Draw the winning screen with the mantis shrimp.
                pygame.draw.rect(self.display_surface, (255, 248, 220),
                                 pygame.Rect(0, 0, 800, 500))
                self.draw_text("Congratulations! You win a mantis shrimp!", 50,
                               (0, 0, 0), (400, 250))
                shrimp = pygame.image.load("graphics/mantis_shrimp.webp")
                self.shrimp = pygame.transform.scale(shrimp, (100, 100))
                self.shrimp_rect = self.shrimp.get_rect(center=(400, 100))
                self.display_surface.blit(self.shrimp, self.shrimp_rect)
                self.gameover = True
            else:
                self.gameover = False

        def update(self):
            """
            Checks if the player is colliding with any tiles.
            """
            self.delete_produce()

    screen = pygame.display.set_mode((800, 400))


    class StartScreen():
        """
        A class to represent the start screen of the game.

        Attributes:
          screen_surface: A screen that serves as a surface to build the
            start screen off of.
          title_surface: The surface of the title text.
          title_rect: The rectangle around the title text to assist in
            placing the title.
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
          start_button: The start button created by scaling a PNG file image.
          rect: The rectangle around the start button to help in placing it.
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
PLAYER_OBJECT = None

def get_player():
    """
    Create a global Player class instance to avoid making multiple instances of
    the same class.

    Returns:
    PLAYER_OBJECT: An instance of the Player class. If the PLAYER_OBJECT has not
    already been created, it is created. If it has, the function returns a
    global instance.
    """
    global PLAYER_OBJECT

    if PLAYER_OBJECT is None:
        PLAYER_OBJECT = GardenModel.Player((380, 160))

    return PLAYER_OBJECT
