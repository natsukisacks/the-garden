""" Creates the map that everything is based upon. """

import pygame
from settings import *
# from player import Player, get_player

class Tile(pygame.sprite.Sprite):
    """
    groups: sprite groups it should be a part of
    """

    def __init__(self, pos):
        # Initiating the parent Sprite class
        super().__init__()
        image = pygame.image.load("tomato.png").convert_alpha()
        self.image = pygame.transform.scale(image, (64, 64))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
      self.rect.x += x_shift

class Level:
  def __init__(self, level_map, surface):
    self.display_surface = surface
    self.setup_level(level_map)
    # self.player = Player((400, 200))  # how to make an instance of the player sprite without drawing it?
      # does this actually create an instance of the player??
    # self.player = get_player()
    # self.player_group = pygame.sprite.Group()
    # self.player_group.add(self.player)

  def setup_level(self, layout):
    self.tiles = pygame.sprite.Group()
    # self.player_group = pygame.sprite.Group()
    # self.player_group.add(self.player)
    
    for row_index, row in enumerate(layout):
      for col_index, col in enumerate(row):
        x = col_index * TILESIZE
        y = row_index * TILESIZE

        if col == "x":
          tile = Tile((x, y))
          self.tiles.add(tile)
        # taking this out for now since it doesn't work with handle_keys. will put back once
        # collisions work.
        # if col == "p":
        #   player_sprite = Player((x, y))
        #   self.player_group.add(player_sprite)
  
  # def get_hits(self, tiles):
  #   """ figure out which tiles are the boundary"""
  #   hits = []
  #   for tile in tiles:
  #     if self.rect.colliderect(tile):
  #       hits.append(tile)
  #   return hits
    
  # def check_collision_x(self, tiles):
    # for tile in tiles:
      # if pygame.sprite.collide_rect(self.player, tile):
      #   print("collided")
    # collisions = self.get_hits(tiles)
    # collided = pygame.sprite.spritecollide(self.player, tiles, False)
      
    # if len(collided) > 0:
    #   print("collided!")
    #   print("in collision_x")
    #   if self.player.x > 0: # hitting a tile while moving right
    #     self.player.x = tile.rect.left - self.rect.w
    #     self.player.rect.x = self.player.x
      # elif player.self.x < 0: # hitting a tile while moving left
      #   self.player.x = tile.rect.right
      #   self.player.rect.x = self.player.x

  # def scroll_x(self):
  #   # player = self.player
  #   player_x = self.player.rect[0]  # getting the center of the x position of the player
  #   direction_x = self.player.dist
  #   self.player.dist = 0
    # if direction_x != 0:
      # print(direction_x)
    
  #   if player_x < 200:
  #     self.world_shift = 8
  #     player.dist = 0
          
  def run(self):
    # self.tiles.update(-1)
    
    # Level tiles
    self.tiles.draw(self.display_surface)
    
    # self.player.draw(self.display_surface)
    
    # self.check_collision_x(self.tiles)
    # self.scroll_x()