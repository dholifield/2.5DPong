import pygame
from time import sleep, time
from pygame.locals import *
from paddle import *
from ball import *
from background import *
from scoreboard import *
from menu import *
#from game import *
from constants import *


def main():
    running = True

    # Pygame initialization
    pygame.init()
    pygame.display.set_caption("2.5D Pong")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    menu_font = pygame.font.Font('fonts/MajorMonoDisplay.ttf', 40)

    # Initializing objects
    ball = Ball()
    #paddle_one = playerPaddle(PADDLE_X, pygame.K_w, pygame.K_s)
    #paddle_two = playerPaddle(WIDTH - PADDLE_X, pygame.K_i, pygame.K_k)
    paddle_one = cpuPaddle(WIDTH - PADDLE_X, ball , 2)
    paddle_two = cpuPaddle(PADDLE_X, ball, 2)

    scoreboard = Scoreboard(21)

    while running:
        t0 = time()
        # Stop running on exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #end

        # Clear screen before each frame
        background_render(screen)

        # Update Objects
        paddle_one.update()
        paddle_two.update()
        ball.paddles(paddle_one, paddle_two)
        ball.update()

        # Scoring
        scoreboard.count(ball, paddle_one, paddle_two)
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

        if dt < 0.002:
            sleep(0.002 - dt)

        #t2 = time()
        #print(f'framerate: {1 / (t2 - t0)}')
    #end
#end

# Runs main code
if __name__ == "__main__":
    main()
