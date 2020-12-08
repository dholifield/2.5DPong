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
    scoreboard = Scoreboard(11)

    while running:
        paddle_one, paddle_two = mainMenu(screen, ball)
        if paddle_one != 0:
            game = Game(ball, scoreboard, paddle_one, paddle_two)
            winner = game.run(screen);

            if winner[2] == 0:
                running = False
            else:
                sleep(1)
                running = winMenu(screen, winner)
        else:
            running = False
        #end
    #end
#end

# Runs main code
if __name__ == "__main__":
    main()
