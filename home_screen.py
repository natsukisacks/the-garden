import pygame

screen = pygame.display.set_mode((800, 400))

class StartScreen():
    def __init__(self): # this should be init
        """ Creates & displays the start screen with a working start button. """
        # Create a display surface
        self.screen_surface = pygame.Surface((800,400))
        # Fill entire background with lavender
        self.screen_surface.fill((230,230,250))
    
        # Title
        title = pygame.font.Font("pixel_text.ttf", 40)
        self.title_surface = title.render("Welcome to the Garden!", False, (115, 79, 150))
        self.title_rect = self.title_surface.get_rect(center = (400, 100))
      
    def draw(self):
        screen.blit(self.screen_surface, (0,0))
        screen.blit(self.title_surface, self.title_rect)

class Button():
    """
    Insert docstring here
    """
    def __init__(self):
        self.start_button = pygame.image.load("start_button.png").convert_alpha()
        self.start_button = pygame.transform.scale(self.start_button, (130, 64))
        self.rect = self.start_button.get_rect()
        self.rect.center = (400, 300)
        self.clicked = False

    def draw(self, surface):
        # Get mouse position
        position = pygame.mouse.get_pos()

        # Check if the mouse point (pos) has collided with the button rectangle.
        if self.rect.collidepoint(position):
            # This method returns an array, so check for the right-most button being clicked.
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                print("CLICKED")

        # Draw the button on the screen
        surface.blit(self.start_button, self.rect)
        
        return self.clicked