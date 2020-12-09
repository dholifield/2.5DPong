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

# Main function that loops through the menus and game
def main():
    running = True

    # Pygame initialization
    pygame.init()
    pygame.display.set_caption("2.5D Pong")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Initializing objects
    ball = Ball()
    scoreboard = Scoreboard(11)

    # Main loop, will run until you close the window or force stop the program
    while running:
        # Calls the main menu and gets paddles
        paddles = mainMenu(screen, ball)
        if paddles[0] != 0:
            # Creates Game object with paddles and runs it
            game = Game(ball, scoreboard, paddles)
            winner = game.run(screen);

            if winner[2] == 0:
                running = False
            else:
                sleep(1)
                # Runs win menu when the game is over, loops back to main menu
                running = winMenu(screen, winner)
        else:
            running = False
        #end
    #end
#end

# Runs main code when file is run. Allows main to be accessed elsewhere
if __name__ == "__main__":
    main()
#end
