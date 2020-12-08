import pygame
from time import sleep, time
from pygame.locals import *
from paddle import *
from ball import *
from background import *
from scoreboard import *
from constants import *

class Game():
    def __init__(self, ball, scoreboard, paddle_one, paddle_two):
        self.paddle_one = paddle_one
        self.paddle_two = paddle_two
        self.ball = ball
        self.scoreboard = scoreboard
    #end

    def run(self, screen):
        running = True
        winner = 0

        self.ball.reset(1)
        self.ball.count = 5
        self.paddle_one.reset()
        self.paddle_two.reset()
        self.scoreboard.reset()

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
            self.ball.paddles(self.paddle_one, self.paddle_two)
            self.ball.update()

            # Scoring
            self.scoreboard.count(self.ball, self.paddle_one, self.paddle_two)
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

            if dt < 0.002:
                sleep(0.002 - dt)

            if self.scoreboard.winner() != 0:
                winner = self.scoreboard.winner()
                running = False
            #end
        #end
        return self.scoreboard.score()
    #end
#end Game
