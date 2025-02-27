import pygame

# Simple setup

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# Set_icon will also change the Icon of the program
pygame.display.set_caption("Space Shooter")
running = True

# surface

surf = pygame.Surface((100,200))
surf.fill('orange')
x = 100

# importing a surface
player_surf = pygame.image.load('space_shooter/images/player.png')

while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the game
    screen.fill('darkgray')
    x += 0.1
    screen.blit(player_surf,(x, 150))
    pygame.display.update()
pygame.quit()