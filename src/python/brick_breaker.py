import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for screen width and height
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
paddle_speed = 10

# Ball settings
BALL_RADIUS = 10
ball_speed_x, ball_speed_y = 5, -5

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Brick Breaker Game")

# Function to draw the paddle
def draw_paddle(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, PADDLE_WIDTH, PADDLE_HEIGHT))

# Function to draw the ball
def draw_ball(x, y):
    pygame.draw.circle(screen, RED, (x, y), BALL_RADIUS)

# Main game loop
def main():
    paddle_x = (SCREEN_WIDTH - PADDLE_WIDTH) // 2  # Center paddle
    paddle_y = SCREEN_HEIGHT - 50  # Position paddle above the bottom
    ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2  # Center ball

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Exit the game
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:  # Move paddle left
            paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < SCREEN_WIDTH - PADDLE_WIDTH:  # Move paddle right
            paddle_x += paddle_speed

        # Update ball position
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Ball collision with walls
        if ball_x <= BALL_RADIUS or ball_x >= SCREEN_WIDTH - BALL_RADIUS:
            ball_speed_x *= -1  # Reverse ball direction on x-axis

        if ball_y <= BALL_RADIUS:  # Ball hits the top wall
            ball_speed_y *= -1

        if ball_y >= SCREEN_HEIGHT - BALL_RADIUS:  # Ball hits the bottom wall
            print("Game Over!")  # Simple game over message
            pygame.quit()
            sys.exit()

        # Ball collision with paddle
        if (paddle_y <= ball_y + BALL_RADIUS <= paddle_y + PADDLE_HEIGHT and
                paddle_x <= ball_x <= paddle_x + PADDLE_WIDTH):
            ball_speed_y *= -1  # Reverse ball direction on y-axis

        # Clear the screen
        screen.fill(BLACK)
        draw_paddle(paddle_x, paddle_y)  # Draw paddle
        draw_ball(ball_x, ball_y)  # Draw ball

        pygame.display.flip()  # Update the display
        clock.tick(60)  # Limit to 60 frames per second

if __name__ == "__main__":
    main()
