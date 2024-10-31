# # Pong game with pygame
# import pygame
# import sys

# # Initialize the game
# pygame.init()

# # Set up the screen
# screen = pygame.display.set_mode((800, 600))

# # Set up color
# BROWN = (225, 118, 47)
# BLUE = (93, 173, 226)
# GRAY = (123, 125, 125)

# # Set up clock
# clock = pygame.time.Clock()

# # Set up paddles
# paddle1 = pygame.Rect(10, 250, 10, 100)
# paddle2 = pygame.Rect(780, 250, 10, 100)

# # Set up ball
# ball = pygame.Rect(400,300,20,20)
# ball_speed_x = 7
# ball_speed_y = 7

# # Game Loop
# playing = True

# while playing:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

# # Move the paddles
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_w]:
#         paddle1.y -= 5
#     if keys[pygame.K_s]:
#         paddle1.y += 5
#     if keys[pygame.K_UP]:
#         paddle2.y -= 5
#     if keys[pygame.K_DOWN]:
#         paddle2.y += 5

# # Move the ball
#     ball.x += ball_speed_x
#     ball.y += ball_speed_y

# # Bounce the ball off the top and bottom walls
#     if ball.top <= 0 or ball.bottom >= 600:
#         ball_speed_y = -ball_speed_y

# # Bounce the ball off the paddles
#     if ball.colliderect(paddle1) or ball.colliderect(paddle2):
#         ball_speed_x = -ball_speed_x

# # Check if the ball goes out of bounds
#     if ball.left <= 0 or ball.right >= 800:
#         ball.x = 400
#         ball.y = 300
#         ball_speed_x = 7
#         ball_speed_y = 7

# # Fill the window with black color
#     screen.fill(BROWN)

# # Draw the paddles and ball
#     pygame.draw.rect(screen, BLUE, paddle1)
#     pygame.draw.rect(screen, BLUE, paddle2)
#     pygame.draw.ellipse(screen, GRAY, ball)

#     pygame.display.update()
#     clock.tick(10)

# Pong game with pygame
import pygame
import sys

# Initialize the game
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))

# Set up color
BROWN = (225, 118, 47)
BLUE = (93, 173, 226)
GRAY = (123, 125, 125)

# Set up clock
clock = pygame.time.Clock()

# Set up paddles
paddle1 = pygame.Rect(10, 250, 10, 100)
paddle2 = pygame.Rect(780, 250, 10, 100)

# Set up ball
ball = pygame.Rect(400,300,20,20)
ball_speed_x = 7
ball_speed_y = 7

# Game Loop
playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.y -= 5
    if keys[pygame.K_s]:
        paddle1.y += 5
    if keys[pygame.K_UP]:
        paddle2.y -= 5
    if keys[pygame.K_DOWN]:
        paddle2.y += 5

# Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

# Bounce the ball off the top and bottom walls
    if ball.top <= 0 or ball.bottom >= 600:
        ball_speed_y = -ball_speed_y

# Bounce the ball off the paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x = -ball_speed_x

# Check if the ball goes out of bounds
    if ball.left <= 0 or ball.right >= 800:
        ball.x = 400
        ball.y = 300
        ball_speed_x = 7
        ball_speed_y = 7

# Fill the window with black color
    screen.fill(BROWN)

# Draw the paddles and ball
    pygame.draw.rect(screen, BLUE, paddle1)
    pygame.draw.rect(screen, BLUE, paddle2)
    pygame.draw.ellipse(screen, GRAY, ball)

    pygame.display.update()
    clock.tick(60)