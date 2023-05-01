import pygame
import sys
from fish import Fish

# Define constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
BG_COLOR = (255, 255, 255)
FPS = 60

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

# Set up the window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fish Schooling Simulation")

# Set up the loading screen
loading_font = pygame.font.SysFont("Arial", 24)
loading_text = loading_font.render("Loading...", True, (0, 0, 0))
loading_rect = loading_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
screen.blit(loading_text, loading_rect)
pygame.display.flip()

# Create the fish
fish_list = []
for i in range(10):
    fish_list.append(Fish(SCREEN_WIDTH,SCREEN_HEIGHT))

# Run the simulation loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the fish positions
    for fish in fish_list:
        fish.update(fish_list)

    # Draw the fish and background
    screen.fill(BG_COLOR)
    for fish in fish_list:
        fish.draw(screen)

    # Update the screen
    pygame.display.flip()
    clock.tick(FPS)
