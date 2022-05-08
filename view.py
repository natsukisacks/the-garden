from model import GardenModel, get_player #Tile, Level, StartScreen, Button, get_player
from settings import *
import pygame

class GardenView():
  def __init__(self, surface):
    self.surface = surface
    self.screen = pygame.display.set_mode((800, 500))
    self.level = GardenModel.Level(WORLD_MAP, self.surface)
    self.player = get_player()
    self.button = GardenModel.Button()
    self.start = GardenModel.StartScreen()
    
  def draw_game(self):
    # self.surface.blit(self.level.background, (0,0))
    self.screen.blit(self.level.background, (0, 0))
    self.level.all_tiles.draw(self.surface)
  
  def draw_player(self):
    self.surface.blit(self.player.player, (self.player.rect.centerx, self.player.rect.centery))
  
  def draw_home(self):
    self.screen.blit(self.start.screen_surface, (0,0))
    self.screen.blit(self.start.title_surface, self.start.title_rect)
    self.screen.blit(self.button.start_button, self.button.rect)