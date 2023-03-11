import pygame
import random

pygame.init()

# Set up the game window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Racing Game")

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the player car
player_car_image = pygame.image.load("images (5).jpeg")
player_car_x = 250
player_car_y = 600
player_car_speed = 0

# Set up the enemy cars
enemy_car_images = [pygame.image.load("download.png"), pygame.image.load("images (5).jpeg"), pygame.image.load("download.png")]
enemy_cars = []
enemy_car_speed = 5
enemy_car_spawn_timer = 0

# Set up the game loop
game_running = True
clock = pygame.time.Clock()

while game_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_car_speed = -5
            if event.key == pygame.K_RIGHT:
                player_car_speed = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_car_speed = 0

    # Update player car position
    player_car_x += player_car_speed
    if player_car_x < 0:
        player_car_x = 0
    if player_car_x > WINDOW_WIDTH - player_car_image.get_width():
        player_car_x = WINDOW_WIDTH - player_car_image.get_width()

    # Spawn enemy cars
    enemy_car_spawn_timer += 1
    if enemy_car_spawn_timer >= 60:
        enemy_car_spawn_timer = 0
        enemy_car_image = random.choice(enemy_car_images)
        enemy_car_x = random.randint(0, WINDOW_WIDTH - enemy_car_image.get_width())
        enemy_car_y = -enemy_car_image.get_height()
        enemy_cars.append((enemy_car_image, enemy_car_x, enemy_car_y))

    # Update enemy car positions
    for i in range(len(enemy_cars)):
        enemy_cars[i] = (enemy_cars[i][0], enemy_cars[i][1], enemy_cars[i][2] + enemy_car_speed)

    # Remove off-screen enemy cars
    enemy_cars = [enemy_car for enemy_car in enemy_cars if enemy_car[2] < WINDOW_HEIGHT]

    # Check for collisions
    for enemy_car in enemy_cars:
        enemy_car_rect = pygame.Rect(enemy_car[1], enemy_car[2], enemy_car[0].get_width(), enemy_car[0].get_height())
        player_car_rect = pygame.Rect(player_car_x, player_car_y, player_car_image.get_width(), player_car_image.get_height())
        if enemy_car_rect.colliderect(player_car_rect):
            game_running = False

    # Draw the game
    game_window.fill(WHITE)
    game_window.blit(player_car_image, (player_car_x, player_car_y))
    for enemy_car in enemy_cars:
        game_window.blit(enemy_car[0], (enemy_car[1], enemy_car[2]))
    pygame.display.update()

    # Set the game clock
    clock.tick(60)

# Clean up the game
pygame.quit()
