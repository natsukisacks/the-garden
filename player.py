import pygame

# put the collide method into this file, 
  # pygame.sprite.spritecollide(self, tiles, False)
class Player(pygame.sprite.Sprite):  # represents the bird, not the game
    def __init__(self, pos):
        """ The constructor of the class """
        pygame.sprite.Sprite.__init__(self)
        # super().__init__()
        image = pygame.image.load("player.png").convert_alpha()
        self.image = pygame.transform.scale(image, (64, 64))
        self.rect = self.image.get_rect(center = pos)
        self.rect.center = pos
        # the player's initial position
        self.x = pos[0]
        self.y = pos[1]
        # self.dist = 0

    # The controller portion of player
    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        self.dist = 5 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]: # down key
            self.y += self.dist # move down
        elif key[pygame.K_UP]: # up key
            self.y -= self.dist # move up
        if key[pygame.K_RIGHT]: # right key
            self.x += self.dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.x -= self.dist # move left
    
    # def check_collision_x(self, tile_image):
    # for tile in tiles:
      # if pygame.sprite.collide_rect(self.player, tile):
      #   print("collided")
    # collisions = self.get_hits(tiles)
      # collided = pygame.sprite.spritecollide(self, tiles, False)
      
    #   if pygame.sprite.collide_rect(self.image, tile_image) is True:
        # print("collided")
      # if len(collided) > 0:
        # print("collided")
    
    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.x, self.y))

player_object = None

def get_player():
  global player_object
  
  if player_object is None:
    player_object = Player((400, 200))
    
  return player_object