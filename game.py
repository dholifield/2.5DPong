import pygame
from time import sleep, time
from pygame.locals import *
from paddle import *
from ball import *
from background import *
from scoreboard import *
from constants import *

# Game Object
class Game():
    # Initialization of game
    def __init__(self, ball, scoreboard, paddles):
        self.paddles = paddles
        self.paddle_one = paddles[0]
        self.paddle_two = paddles[1]
        self.ball = ball
        self.scoreboard = scoreboard
    #end

    # Main loop of game where gameplay happens
    def run(self, screen):
        running = True
        winner = 0

        # Resets ball, paddles, and scoreboard from possible previous games
        self.ball.reset(1)
        self.ball.count = 5
        self.paddle_one.reset()
        self.paddle_two.reset()
        self.scoreboard.reset()

        # Main Game loop
        while(running):
            t0 = time()

            # Stop running on exit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            #end

            # Clear screen before each frame
            background_render(screen)

            # Update Objects
            self.paddle_one.update()
            self.paddle_two.update()
            self.ball.paddleCollide(self.paddles)
            self.ball.update()

            # Scoring
            self.scoreboard.count(self.ball)
            if self.ball.count == 1:
                self.paddle_one.reset()
                self.paddle_two.reset()
            #end

            # Render objects
            self.paddle_one.render(screen)
            self.paddle_two.render(screen)
            self.ball.render(screen)
            self.scoreboard.render(screen)

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
            if self.scoreboard.winner() != 0:
                winner = self.scoreboard.winner()
                running = False
            #end
        #end
        return self.scoreboard.score()
    #end
#end Game
