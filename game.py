import pygame
from time import sleep, time
from pygame.locals import *
from paddle import *
from ball import *
from background import *
from scoreboard import *
from constants import *

# Main loop of game where gameplay happens
def game(screen, ball, scoreboard, paddles):
    # Initialization of paddles
    paddle_one = paddles[0]
    paddle_two = paddles[1]

    running = True

    # Resets ball, paddles, and scoreboard from possible previous games
    ball.reset(1)
    ball.count = 5
    paddle_one.reset()
    paddle_two.reset()
    scoreboard.reset()

    # Main Game loop
    while(running):
        t0 = time()

        # Stop running on exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #end

        # Clear screen before each frame
        drawBackground(screen)

        # Update Objects
        paddle_one.update()
        paddle_two.update()
        ball.paddleCollide(paddles)
        ball.update()

        # Scoring
        scoreboard.count(ball)
        if ball.count == 1:
            paddle_one.reset()
            paddle_two.reset()
        #end

        # Render objects
        paddle_one.render(screen)
        paddle_two.render(screen)
        ball.render(screen)
        scoreboard.render(screen)

        # Display frame
        display_surface = pygame.display.get_surface()
        display_surface.blit(pygame.transform.flip(display_surface, False, True), dest=(0, 0))
        pygame.display.flip()

        t1 = time()
        dt = t1 - t0

        # Timer for consistant frames per second
        if dt < 0.002:
            sleep(0.002 - dt)

        # Stop running when there is a winner
        if scoreboard.winner() != 0:
            running = False
        #end
    #end
    return scoreboard.score()
#end game
