import pygame
from pygame.locals import *
from constants import *

# Button Object
class Button():
    # Preset values for a button
    button_col = WHITE
    hover_col = GRAY
    text_col = GRAY
    click_col = LIGHT_GRAY

    clicked = False
    space = 0

    # Initialization of button with location, size, and text
    def __init__(self, x, y, size, text):
        self.x = x
        self.y = y
        self.text = text
        self.size = size
    #end

    # Draws button and returns true if button is pressed
    def draw(self, screen):
        action = False

        pos = (pygame.mouse.get_pos()[0], HEIGHT - pygame.mouse.get_pos()[1])

        # Creates rectangles for button, collision, and shaddow
        button_rect = Rect((0,0), self.size)
        collision = Rect(0,0, self.size[0], self.size[1] + self.space)
        shaddow = Rect((0,0), self.size)

        button_rect.center = (self.x, self.y + self.space)
        collision.center = (self.x , self.y + self.space / 2)
        shaddow.center = (self.x, self.y)

        # Checks if button is hovered over or pressed
        if collision.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                self.space = 4
            elif pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
                self.clicked = False
                action = True
            else:
                self.space = 8
        else:
            self.space = 0
            self.clicked = False
        #end

        # Draws button, shaddow, and text
        pygame.draw.rect(screen, self.hover_col, shaddow)
        pygame.draw.rect(screen, self.button_col, button_rect)

        font = pygame.font.Font('fonts/MajorMonoDisplay.ttf', 35)
        text_img = font.render(self.text, True, self.text_col)
        text_img = pygame.transform.flip(text_img, False, True)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x - text_len / 2, self.y - 17 + self.space))

        return action
    #end
#end Button
