import pygame
from time import sleep, time
from pygame.locals import *
from paddle import *
from ball import *
from background import *
from scoreboard import *
from menu import *
from game import *
from constants import *

def main():
    running = True

    # Pygame initialization
    pygame.init()
    pygame.display.set_caption("2.5D Pong")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Initializing objects
    ball = Ball()
    scoreboard = Scoreboard(2)
    #paddle_one = playerPaddle(PADDLE_X, pygame.K_w, pygame.K_s)
    #paddle_two = playerPaddle(WIDTH - PADDLE_X, pygame.K_i, pygame.K_k)
    #paddle_one = cpuPaddle(WIDTH - PADDLE_X, ball , 2)
    #paddle_two = cpuPaddle(PADDLE_X, ball, 2)

    #paddle_one, paddle_two = mainMenu(ball)

    while running:
        paddle_one, paddle_two = mainMenu(ball, screen)
        game = Game(ball, scoreboard, paddle_one, paddle_two)

        scoreboard.reset()
        winner = game.run(screen);
        print(winner)
    #end
#end

# Runs main code
if __name__ == "__main__":
    main()
