"""
Garden controller class. Everything in this file contains elements belonging
to the controller portion of the MVC architecture.
"""
import pygame
from model import GardenModel, get_player


class GardenController():
    """
    This class contains everything necessary to update the model and control
    the game.

    Attributes:
      self.clicked: A boolean representing whether the start button has been
        clicked or not.
      self.button: A class instance of the Button class within the GardenModel
        class.
      self.player: A global instance of the player class.
    """
    def __init__(self):
        """
        Constructs all necessary attributes for the controller class.
        """
        # For use in update_button
        self.clicked = False
        self.button = GardenModel.Button()
        self.player = get_player()

    def update_button(self):
        """
        Updates the status of the button.

        Returns:
            self.clicked: True if the start button was clicked and False if it
              wasn't. This boolean indicates to the program whether it should
              display the game next.
        """
        # Get mouse position
        position = pygame.mouse.get_pos()

        # Check if mouse point (pos) has collided with button rectangle.
        if self.button.rect.collidepoint(position):
            # This method returns an array; check for right-most button.
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                print("CLICKED")

        return self.clicked

    def handle_keys(self):
        """
        Handles the keys of the player sprite. This method ensures that, if a
        certain key is pressed (the up, down, left, or right arrows), the player
        sprite moves across the background accordingly.
        """
        key = pygame.key.get_pressed()
        self.player.dist = 3 # distance moved in 1 frame

        if key[pygame.K_DOWN] and self.player.rect.centery < 400: # down key
            self.player.rect.centery += self.player.dist # move down
        elif key[pygame.K_UP] and self.player.rect.centery > 70: # up key
            self.player.rect.centery -= self.player.dist # move up
        if key[pygame.K_RIGHT] and self.player.rect.centerx < 736: # right key
            self.player.rect.centerx += self.player.dist # move right
        elif key[pygame.K_LEFT] and self.player.rect.centerx > 70: # left key
            self.player.rect.centerx -= self.player.dist # move left
