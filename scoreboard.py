import pygame
from pygame.locals import *
from constants import *

# Scoreboard Object
class Scoreboard:
    # Preset values for a scoreboard
    score_one = 0
    score_two = 0

    # Initialization of scoreboard with max score
    def __init__(self, max):
        self.max = max
    #end

    # Counts each time a ball is scored
    def count(self, ball):
        if ball.scored():
            self.add(ball.possession)
            ball.switchPossession()
            ball.reset(ball.possession)
    #end

    # Returns the score
    def score(self):
        return self.score_one, self.score_two, self.winner()
    #end

    # Adds a point to a player
    def add(self, player):
        if player == 2:
            self.score_one = self.score_one + 1
        elif player == 1:
            self.score_two = self.score_two + 1
    #end

    # Returns 1 or 2 when a player has won, otherwise 0
    def winner(self):
        winner = 0

        if self.score_one == self.max:
            winner = 1
        elif self.score_two == self.max:
            winner = 2
        return winner
    #end

    # Resets the score
    def reset(self):
        self.score_one = 0
        self.score_two = 0
    #end

    # Renders the score to the screen
    def render(self, screen):
        font = pygame.font.Font('fonts/RobotoMono.ttf', 40)

        player_one = font.render(str(self.score_one), True, WHITE)
        player_two = font.render(str(self.score_two), True, WHITE)
        player_one = pygame.transform.flip(player_one, False, True)
        player_two = pygame.transform.flip(player_two, False, True)

        x1 = len(str(abs(self.score_one))) - 1
        x2 = len(str(abs(self.score_two))) - 1
        screen.blit(player_one, (CENTER_X - 50 - x1 * 14, HEIGHT - 48))
        screen.blit(player_two, (CENTER_X + 28 - x2 * 14, HEIGHT - 48))
    #end
#end Scoreboard
