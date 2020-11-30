import pygame
from pygame.locals import *
from constants import *

table = Rect(0,0, TABLE_LENGTH, TABLE_WIDTH)
table_shaddow = Rect(0,0, TABLE_LENGTH, TABLE_HEIGHT)
net = Rect(0,0, NET_LENGTH, TABLE_WIDTH)
net_shaddow = Rect(0,0, NET_LENGTH, NET_HEIGHT)

leg = Rect(0,0, 30, 100)

line = Rect(0,0, 7, TABLE_WIDTH)

scoreboard = Rect(0,0, SCOREBOARD_WIDTH, SCOREBOARD_HEIGHT)
border = Rect(0,0, SCOREBOARD_WIDTH + 2 * SCOREBOARD_BORDER, SCOREBOARD_HEIGHT + SCOREBOARD_BORDER)
scoreboard_line = Rect(0,0, SCOREBOARD_BORDER, SCOREBOARD_HEIGHT + SCOREBOARD_BORDER)

def background_render(screen):
    # Background
    screen.fill(GREEN)

    # Table
    table.center = CENTER
    pygame.draw.rect(screen, LIGHT_BLUE, table)
    table_shaddow.center = (CENTER_X, (HEIGHT - TABLE_WIDTH - TABLE_HEIGHT) / 2)
    pygame.draw.rect(screen, DARK_BLUE, table_shaddow)

    '''
    leg.center = (250, (HEIGHT - TABLE_WIDTH - 100) / 2 - TABLE_HEIGHT)
    pygame.draw.rect(screen, BROWN, leg)
    leg.centerx = WIDTH - 250
    pygame.draw.rect(screen, BROWN, leg)
    '''

    # Net
    net.center = (CENTER_X, CENTER_Y + NET_HEIGHT)
    net_shaddow.centerx = CENTER_X
    net_shaddow.y = CENTER_Y - TABLE_WIDTH / 2
    pygame.draw.rect(screen, WHITE, net)
    pygame.draw.rect(screen, LIGHT_GRAY, net_shaddow)

    # Table Lines
    line.center = (300, CENTER_Y)
    pygame.draw.rect(screen, BLUE, line)
    line.centerx = WIDTH - 300
    pygame.draw.rect(screen, BLUE, line)

    # Scoreboard Background
    scoreboard.center = (CENTER_X, HEIGHT - SCOREBOARD_HEIGHT / 2)
    border.center = (CENTER_X, HEIGHT - (SCOREBOARD_HEIGHT + SCOREBOARD_BORDER) / 2)
    scoreboard_line.center = (CENTER_X, HEIGHT - SCOREBOARD_HEIGHT / 2)
    pygame.draw.rect(screen, BROWN, border)
    pygame.draw.rect(screen, ORANGE, scoreboard)
    pygame.draw.rect(screen, BROWN, scoreboard_line)
#end
