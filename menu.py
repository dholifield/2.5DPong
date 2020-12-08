import pygame
from time import sleep
from pygame.locals import *
from button import *
from paddle import *
from constants import *



def mainMenu(screen, ball):
    running = True
    mode = 0
    difficulty = 2
    hover = False

    font = pygame.font.Font('fonts/MajorMonoDisplay.ttf', 100)
    ball_sound = pygame.mixer.Sound('sounds/hit_table.wav')

    one_player = Button(CENTER_X, 420, BUTTON_SIZE, "one player")
    two_player = Button(CENTER_X, 260, BUTTON_SIZE, "two player")
    zero_player = Button(CENTER_X, 100, BUTTON_SIZE, "zero player")

    P = Rect(0,0, 58, 73)
    P.center = (788, 605)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #endm

        screen.fill(GREEN)
        title = font.render("2.5D Pong", True, WHITE)
        title = pygame.transform.flip(title, False, True)
        screen.blit(title, ((WIDTH - title.get_width()) / 2, HEIGHT - 160))

        if one_player.draw(screen):
            mode = 1
        elif two_player.draw(screen):
            mode = 2
        elif zero_player.draw(screen):
            mode = 3
        #end

        # Display frame
        display_surface = pygame.display.get_surface()
        display_surface.blit(pygame.transform.flip(display_surface, False, True), dest=(0, 0))
        pygame.display.flip()

        pos = (pygame.mouse.get_pos()[0], HEIGHT - pygame.mouse.get_pos()[1])
        if P.collidepoint(pos) and hover == False:
            ball_sound.play()
            hover = True
        elif P.collidepoint(pos) == False and hover == True:
            hover = False
        #end


        sleep(0.01)

        if mode != 0:
            running = False
        #end
    #end

    if mode == 2:
        paddle_one = playerPaddle(PADDLE_X, pygame.K_w, pygame.K_s)
        paddle_two = playerPaddle(WIDTH - PADDLE_X, pygame.K_i, pygame.K_k)
    elif mode == 1:
        paddle_one = playerPaddle(PADDLE_X, pygame.K_w, pygame.K_s)
        paddle_two = cpuPaddle(WIDTH - PADDLE_X, ball, difficulty)
    elif mode == 3:
        paddle_one = cpuPaddle(PADDLE_X, ball , difficulty)
        paddle_two = cpuPaddle(WIDTH - PADDLE_X, ball, difficulty)
    else:
        paddle_one, paddle_two = 0, 0
    #end

    return paddle_one, paddle_two
#end


def winMenu(screen, winner):
    running = True
    run = True
    font = pygame.font.Font('fonts/MajorMonoDisplay.ttf', 100)
    large_font = pygame.font.Font('fonts/MajorMonoDisplay.ttf', 200)

    main = Button(CENTER_X, 100, BUTTON_SIZE, "main menu")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                run = False
        #end

        screen.fill(GREEN)

        if winner[2] == 1:
            text = "player one wins!"
        else:
            text = "player two wins!"
        #end

        score_txt = ":"

        title = font.render(text, True, WHITE)
        score = large_font.render(":", True, WHITE)
        title = pygame.transform.flip(title, False, True)
        score = pygame.transform.flip(score, False, True)
        screen.blit(title, ((WIDTH - title.get_width()) / 2, HEIGHT - 140))
        screen.blit(score, ((WIDTH - score.get_width()) / 2, HEIGHT - 440))

        score = large_font.render(str(winner[0]), True, WHITE)
        score = pygame.transform.flip(score, False, True)
        screen.blit(score, ((WIDTH - score.get_width()) / 2 - 330, HEIGHT - 440))

        score = large_font.render(str(winner[1]), True, WHITE)
        score = pygame.transform.flip(score, False, True)
        screen.blit(score, ((WIDTH - score.get_width()) / 2 + 330, HEIGHT - 440))

        if main.draw(screen):
            running = False
        #end

        display_surface = pygame.display.get_surface()
        display_surface.blit(pygame.transform.flip(display_surface, False, True), dest=(0, 0))
        pygame.display.flip()
    #end
    return run
#end
