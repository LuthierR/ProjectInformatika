import pygame
import sys
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 400, 500
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Objects")

# Load and scale the player image
player_image = pygame.image.load("plane.png")
player_width, player_height = 40, 40  # Desired player size
player_image = pygame.transform.scale(player_image, (player_width, player_height))
player_rect = player_image.get_rect()
player_rect.center = (WIDTH // 2, HEIGHT - player_height // 2)

# Falling objects
object_size = 20
object_speed = 10

# Store the falling objects' information in a list
falling_objects = []

def create_falling_object():
    x = random.randint(0, WIDTH - object_size)
    y = 0
    return {'x': x, 'y': y}

def draw_falling_objects(falling_objects):
    for obj in falling_objects:
        pygame.draw.rect(screen, WHITE, (obj['x'], obj['y'], object_size, object_size))

# Game variables
score = 0
game_over = False

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5

    # Clear the screen
    screen.fill(BLACK)

    # Draw the player
    screen.blit(player_image, player_rect)

    # Create and update falling objects
    if random.randint(1, 100) < 5:
        falling_objects.append(create_falling_object())

    for obj in falling_objects:
        obj['y'] += object_speed

    draw_falling_objects(falling_objects)

    # Check for collisions
    for obj in falling_objects:
        if player_rect.colliderect(pygame.Rect(obj['x'], obj['y'], object_size, object_size)):
            game_over = True

    # Remove objects that have gone off-screen
    falling_objects = [obj for obj in falling_objects if obj['y'] <= HEIGHT]

    # Update the score
    score += len(falling_objects)  # Score increases as more objects fall

    # Display the score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
