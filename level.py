import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug

class Level:
  def __init__(self):
    self.display_surface = pygame.display.get_surface()

    # All sprites that need to be drawn on the screen
    self.visible_sprites = pygame.sprite.Group()

    # All sprites that the player can collide with
    self.obstacle_sprites = pygame.sprite.Group()

    self.create_map()

  def create_map(self):
    """
    converting world map into position
    """
    for row_index, row in enumerate(WORLD_MAP):
      for col_index, col in enumerate(row):
        x = col_index * TILESIZE
        y = row_index * TILESIZE

        if col == "x":      
          Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
        if col == "p":
          # the player is no in obstacle sprites
          self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)

  def run(self):
    # update and draw game
    self.visible_sprites.draw(self.display_surface)
    self.visible_sprites.update()
    debug(self.player.direction)  # not able to get keyboard inputs from repl.it