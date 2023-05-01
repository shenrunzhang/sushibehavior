import pygame
import random
import math

# Define constants
FISH_IMG = pygame.image.load("assets/fish.png")
MAX_SPEED = 5
REPULSION_CONSTANT = 0.5

class Fish:
    def __init__(self, bgd_width, bgd_height):
        self.bgd_width = bgd_width
        self.bgd_height = bgd_height
        self.image = FISH_IMG
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, self.bgd_width)
        self.rect.y = random.randrange(0, self.bgd_height)
        self.vx = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.vy = random.uniform(-MAX_SPEED, MAX_SPEED)
        self.ax = 0
        self.ay = 0

    def update(self, fish_list):
        # Calculate forces
        repulsion_force = self.calculate_repulsion(fish_list)

        # Move the fish
        self.rect.x += self.vx
        self.rect.y += self.vy

        # Update velocity  
        self.vx += self.ax
        self.vy += self.ay

        # Update acceleration
        self.ax += repulsion_force[0]
        self.ay += repulsion_force[1]

        # Limit the acceleration to the maximum speed
        if self.ax ** 2 + self.ay ** 2 > MAX_SPEED ** 2:
            scale = MAX_SPEED / (self.ax ** 2 + self.ay ** 2) ** 0.5
            self.ax *= scale
            self.ay *= scale

        # Bounce off the edges of the screen
        if self.rect.left < 0 or self.rect.right > self.bgd_width:
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > self.bgd_height:
            self.vy = -self.vy

    def calculate_repulsion(self, fish_list):
        closest_distance = float('inf')
        closest_fish = None

        for fish in fish_list:
            if fish == self:
                continue
            distance = ((fish.rect.x - self.rect.x) ** 2 + (fish.rect.y - self.rect.y) ** 2) ** 0.5
            if distance < closest_distance :
                closest_fish = fish
                closest_distance = distance

        if closest_distance == 0:
            return (0,0)
        
        dx = closest_fish.rect.x - self.rect.x
        dy = closest_fish.rect.y - self.rect.y


        return (REPULSION_CONSTANT * dx / closest_distance ** 2, REPULSION_CONSTANT * dy / closest_distance ** 2  )

    def draw(self, surface):
        # Determine the angle of rotation based on the velocity vector
        angle = math.degrees(math.atan2(self.vy, self.vx)) + 180

        # Rotate the image and draw it onto the surface
        rotated_image = pygame.transform.rotate(self.image, angle)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        surface.blit(rotated_image, rotated_rect)