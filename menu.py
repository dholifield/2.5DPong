import pygame
from time import sleep
from pygame.locals import *
from button import *
from paddle import *
from constants import *

# Main menu where user selects game option
def mainMenu(screen, ball):
    running = True
    mode = 0
    difficulty = 2
    hover = False

    # Creates font for text and sound
    font = pygame.font.Font('fonts/MajorMonoDisplay.ttf', 100)
    ball_sound = pygame.mixer.Sound('sounds/hit_table.wav')

    # Creates three buttons for different play modes
    one_player = Button(CENTER_X, 420, BUTTON_SIZE, "one player")
    two_player = Button(CENTER_X, 260, BUTTON_SIZE, "two player")
    zero_player = Button(CENTER_X, 100, BUTTON_SIZE, "zero player")

    # Creates a rectangle for ball sound
    O = Rect(0,0, 58, 73)
    O.center = (788, 605)

    # Main menu loop
    while running:
        # Ends loop if you close window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #endm

        # Fills the screen green and displays the title
        screen.fill(GREEN)
        title = font.render("2.5D Pong", True, WHITE)
        title = pygame.transform.flip(title, False, True)
        screen.blit(title, ((WIDTH - title.get_width()) / 2, HEIGHT - 160))

        # Draws the 3 buttons and checking if any are pressed
        if one_player.draw(screen):
            mode = 1
        elif two_player.draw(screen):
            mode = 2
        elif zero_player.draw(screen):
            mode = 3
        #end


        # Display the frame
        display_surface = pygame.display.get_surface()
        display_surface.blit(pygame.transform.flip(display_surface, False, True), dest=(0, 0))
        pygame.display.flip()

        # Get posistion of cursor and make a noise if it collides the the O
        pos = (pygame.mouse.get_pos()[0], HEIGHT - pygame.mouse.get_pos()[1])
        if O.collidepoint(pos) and not hover:
            ball_sound.play()
            hover = True
        elif not O.collidepoint(pos) and hover:
            hover = False
        #end

        # Timer to prvent unnecessary stress on hardware
        sleep(0.01)

        # If a button is pressed, end the loop
        if mode != 0:
            running = False
        #end
    #end

    # Create paddles objects based on user selection
    if mode == 2:
        paddle_one = playerPaddle(PADDLE_X, pygame.K_w, pygame.K_s)
        paddle_two = playerPaddle(WIDTH - PADDLE_X, pygame.K_o, pygame.K_k)
    elif mode == 1:
        paddle_one = playerPaddle(PADDLE_X, pygame.K_w, pygame.K_s)
        paddle_two = cpuPaddle(WIDTH - PADDLE_X, ball, difficulty)
    elif mode == 3:
        paddle_one = cpuPaddle(PADDLE_X, ball , difficulty)
        paddle_two = cpuPaddle(WIDTH - PADDLE_X, ball, difficulty)
    else:
        paddle_one, paddle_two = 0, 0
    #end

    # Return the two paddles
    return paddle_one, paddle_two
#end mainMenu

# Winner menu when the game has ended
def winMenu(screen, winner):
    running = True
    run = True

    # Creates Font for text
    font = pygame.font.Font('fonts/MajorMonoDisplay.ttf', 100)
    large_font = pygame.font.Font('fonts/MajorMonoDisplay.ttf', 200)

    # Creates button to return to the main menu
    main = Button(CENTER_X, 100, BUTTON_SIZE, "main menu")

    # Sets text for winner
    text = "player one wins!" if winner[2] == 1 else "player two wins!"

    # Winner Menu Loop
    while running:
        # Ends loop if you close window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                run = False
        #end

        # Fills the screen green
        screen.fill(GREEN)

        # Prints out the winner as well as the score
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

        # Draws button and stops running when pressed
        if main.draw(screen):
            running = False
        #end

        # Display the frame
        display_surface = pygame.display.get_surface()
        display_surface.blit(pygame.transform.flip(display_surface, False, True), dest=(0, 0))
        pygame.display.flip()

        # Timer to prvent unnecessary stress on hardware
        sleep(0.01)
    #end
    return run
#end winMenu
