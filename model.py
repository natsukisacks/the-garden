import pygame

class Button():
    """
    Insert docstring here
    """
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self, surface):
        action = False

        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Check mouse behavior
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                print("CLICKED")

        # Allow the button to be pressed multiple times
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
                action = True
        # Draw the button on the screen
        surface.blit(self.image, self.rect)

        return action

def title_screen(screen):
    # Create a display surface
    screen_surface = pygame.Surface((800,400))
    # Fill entire background with lavender
    screen_surface.fill((230,230,250))

    # Title
    title = pygame.font.Font("pixel_font.ttf", 40)
    title_surface = title.render("Welcome to the Garden!", False, (115, 79, 150))
    title_rect = title_surface.get_rect(center = (400, 100))

    # Might need to make another class for the player sprite
    player = pygame.image.load("player_sprite.png").convert_alpha()
    player_rect = player.get_rect(center = (400, 200))

    # Start button
    start_button_img = pygame.image.load("start_button.png").convert_alpha()
    start_button = Button(100, 200, start_button_img)

    screen.blit(screen_surface, (0,0))
    screen.blit(title_surface, title_rect)
    screen.blit(player, player_rect)
    start_button.draw()