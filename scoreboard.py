import pygame
from pygame.locals import *
from constants import *

class Scoreboard:
    def __init__(self, max):
        self.score_one = 0
        self.score_two = 0

        self.max = max
    #end

    # Counts each time a ball is scored
    def count(self, ball, paddle_one, paddle_two):
        if ball.scored():
            self.add(ball.possession)
            ball.switchPossession()
            ball.reset(ball.possession)
    #end

    # Adds a point to a player
    def add(self, player):
        if player == 2:
            self.score_one = self.score_one + 1
        elif player == 1:
            self.score_two = self.score_two + 1
    #end

    # Add while loop with pop-up to reset or go to main menu
    def winner(self):
        if self.score_one == self.max:
            pass
    #end

    # Resets the score
    def reset(self):
        self.score_one = 0
        self.score_two = 0
    #end

    # Renders the score to the screen
    def render(self, screen):
        font = pygame.font.Font('fonts/RobotoMono.ttf', 40)

        self.player_one = font.render(str(self.score_one), True, WHITE)
        self.player_two = font.render(str(self.score_two), True, WHITE)
        self.player_one = pygame.transform.flip(self.player_one, False, True)
        self.player_two = pygame.transform.flip(self.player_two, False, True)

        x1 = len(str(abs(self.score_one))) - 1
        x2 = len(str(abs(self.score_two))) - 1
        screen.blit(self.player_one, (CENTER_X - 50 - x1 * 14, HEIGHT - 48))
        screen.blit(self.player_two, (CENTER_X + 28 - x2 * 14, HEIGHT - 48))
    #end
#end Scoreboard
