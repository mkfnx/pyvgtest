import sys

import pygame
import random

from Mole import Mole


def update_mole_position():
    pass


WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
BACKGROUND_COLOR = (255, 255, 255)
GRID_SIZE = 64
NUM_ROWS = 4
NUM_COLS = 6

pygame.init()

game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Whack-a-Monster")
game_window.fill(BACKGROUND_COLOR)

# Create the holes grid
holes = []
for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        x = col * GRID_SIZE
        y = row * GRID_SIZE
        rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
        holes.append(rect)

# Create the mole Rect object
mole_visible = False
mole_image = pygame.image.load("slime.png")
mole = Mole(100, 100, GRID_SIZE // 2, mole_image)
mole_move_event = pygame.USEREVENT + 1
pygame.time.set_timer(mole_move_event, 1000)

# Set up the clock
clock = pygame.time.Clock()
score = 0

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == mole_move_event:
            mole_visible = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mole_visible and mole.collidepoint(event.pos):
                mole_visible = False
                score += 1

    # Update the mole visibility
    if not mole_visible:
        # Choose a random hole for the mole to appear in
        hole = random.choice(holes)
        mole.topleft = hole.topleft
        mole_visible = True

    # Draw the background and holes grid
    game_window.fill(BACKGROUND_COLOR)
    for hole in holes:
        pygame.draw.rect(game_window, (0, 0, 0), hole)

    # Draw the mole if it's visible
    if mole_visible:
        # pygame.draw.circle(game_window, (255, 0, 0), mole.center, GRID_SIZE // 2)
        mole.draw(game_window)

    # draw the score display
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: {}".format(score), True, (255, 255, 255))
    game_window.blit(score_text, (10, 10))

    # Update the display and wait for the next frame
    pygame.display.update()
    clock.tick(30)
