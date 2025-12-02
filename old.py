import pygame

# Initialize Pygame
pygame.init()

# Screen setup
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mini Shooter")

# Player setup
player_x, player_y = width//2, height - 50
player_speed = 5

# Bullets
bullets = []
bullet_speed = 7

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # 60 FPS
    screen.fill((0, 0, 0))  # Clear screen

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullets.append([player_x + 15, player_y])  # shoot bullet

    # Keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - 30:
        player_x += player_speed

    # Update bullets
    for b in bullets[:]:
        b[1] -= bullet_speed
        if b[1] < 0:
            bullets.remove(b)
        else:
            pygame.draw.rect(screen, (255, 255, 0), (*b, 5, 10))  # draw bullet

    # Draw player
    pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, 30, 30))

    pygame.display.flip()

pygame.quit()
