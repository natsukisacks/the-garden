import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
  """
  groups: sprite groups it should be a part of
  """
  def __init__(self, position, groups):
    # Initiating the parent Sprite class
    super().__init__(groups)
    image = pygame.image.load("pomegranate pixel.png").convert_alpha()
    self.image = pygame.transform.scale(image, (64, 64))
    self.rect = self.image.get_rect(topleft = position)