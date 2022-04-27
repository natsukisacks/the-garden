import pygame
from settings import *

class Player(pygame.sprite.Sprite):
  """
  groups: sprite groups it should be a part of
  """
  def __init__(self, position, groups, obstacle_sprites):
    # Initiating the parent Sprite class
    super().__init__(groups)
    image = pygame.image.load("player_sprite.png").convert_alpha()
    self.image = pygame.transform.scale(image, (64, 64))
    self.rect = self.image.get_rect(topleft = position)

    self.direction = pygame.math.Vector2()
    self.speed = 5 # replace w player dictionary later

    self.obstacle_sprites = obstacle_sprites
  def input(self):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
      self.direction.y = -1
    elif keys[pygame.K_DOWN]:
      self.direction.y = 1
    else:
      # Ensure that the player doesn't continue after the key as been lifted
      self.direction.y = 0

    if keys[pygame.K_LEFT]:
      self.direction.y = -1
    elif keys[pygame.K_RIGHT]:
      self.direction.y = 1
    else:
      self.direction.x = 0

  def move(self, speed):
    if self.direction.magnitude() != 0:
      # set magnitude to 1
      self.direction = self.direction.normalize()
    # self.rect.center += self.direction * speed
    self.rect.x += self.direction.x * speed
    self.collision("horizontal")
    self.rect.y += self.direction.y * speed
    self.collision("vertical")

  def collision(self, direction):
    if direction == "horizontal":
      for sprite in self.obstacle_sprites:
        # will tell us if there's a collision
        if sprite.rect.colliderect(self.rect):
          # horizontal collisions
          if self.direction.x > 0:  # moving right
            self.rect.right = sprite.rect.left
          if self.direction.x < 0:  # moving left
            self.rect.left = sprite.rect.right 
    # vertical collisions
    if direction == "vertical":
      for sprite in self.obstacle_sprites:
          if self.direction.y > 0: # moving down
            self.rect.bottom = sprite.rect.top
          if self.direction.y < 0: # moving up
            self.rect.top = sprite.rect.bottom
          
    if direction == "vertical":
      pass
    
  def update(self):
    self.input() # what does this do?
    self.move(self.speed)