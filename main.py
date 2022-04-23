import pygame
from sys import exit

# Initialize pygame
pygame.init()

# Create just a black screen
screen = pygame.display.set_mode((800, 400))

# Help control the frame rate/time
clock = pygame.time.Clock()

# Create a display surface that is always shown. Can't be hidden.
test_surface = pygame.Surface((100, 200))
test_surface.fill("Green")

while True:
    # Create an event loop that checks if the user wants to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # Prevent a coding error

    screen.blit(test_surface, (200, 100)) # Change where the display surface is
    # Display the screen
    pygame.display.update()
    clock.tick(60)