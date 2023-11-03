import pygame
import sys
import random


pygame.init()


WIDTH, HEIGHT = 400, 500
FPS = 60


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Objects")

# Player
player_size = 20
plane = pygame.image.load("plane.png")
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 2 * player_size
# a
object_size = 20
object_x = random.randint(0, WIDTH - object_size)
object_y = 0
object_speed = 5


score = 0
game_over = False



while not game_over:
    player_image = pygame.image.load("plane.png")
    player_rect = player_image.get_rect()
    player_rect.center = (WIDTH // 2, HEIGHT - player_image.get_height() // 2)
    # screen.blit(player_image(100,100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5


    object_y += object_speed
 

  
    screen.fill(BLACK)



    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, WHITE, (object_x, object_y, object_size, object_size))


    # Check 
    # a
    if (
        player_x < object_x + object_size
        and player_x + player_size > object_x
        and player_y < object_y + object_size
        and player_y + player_size > object_y
    ):
        game_over = True

    if object_y > HEIGHT:
        object_x = random.randint(0, WIDTH - object_size)
        object_y = 0
        score += 1
    game_over = True
    # a
    if object_y > HEIGHT:
        object_x = random.randint(0, WIDTH - object_size)
        object_y = 0
        score += 1
    

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
sys.exit()
