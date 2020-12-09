import pygame
from pygame.locals import *
from constants import *
from shadow import drawShadow

# Rectangles that makeup the table and net
table = Rect(0,0, TABLE_LENGTH, TABLE_WIDTH)
table_edge = Rect(0,0, TABLE_LENGTH, TABLE_HEIGHT)
table_shadow = Rect(0,0, TABLE_LENGTH - 50, TABLE_SHADOW_WIDTH)
leg = Rect(0,0, 30, LEG_HEIGHT)
line = Rect(0,0, 7, TABLE_WIDTH)
net = Rect(0,0, NET_LENGTH, TABLE_WIDTH)
net_shadow = Rect(0,0, NET_LENGTH, NET_HEIGHT)

# Rectangles for the scoreboard and border
scoreboard = Rect(0,0, SCOREBOARD_WIDTH, SCOREBOARD_HEIGHT)
border = Rect(0,0, SCOREBOARD_WIDTH + 2 * SCOREBOARD_BORDER, SCOREBOARD_HEIGHT + SCOREBOARD_BORDER)
scoreboard_line = Rect(0,0, SCOREBOARD_BORDER, SCOREBOARD_HEIGHT + SCOREBOARD_BORDER)

# Renders the background including the ground, the table, and the scoreboard background
def background_render(screen):
    # Background
    screen.fill(GREEN)

    # Table Legs
    leg.center = (250, (HEIGHT - TABLE_WIDTH - LEG_HEIGHT) / 2 - TABLE_HEIGHT)
    pygame.draw.rect(screen, BROWN, leg)
    leg.centerx = WIDTH - 250
    pygame.draw.rect(screen, BROWN, leg)

    # Table
    table.center = CENTER
    pygame.draw.rect(screen, LIGHT_BLUE, table)
    table_edge.center = (CENTER_X, (HEIGHT - TABLE_WIDTH - TABLE_HEIGHT) / 2)
    pygame.draw.rect(screen, DARK_BLUE, table_edge)
    table_shadow.center = (CENTER_X, CENTER_Y - TABLE_WIDTH / 2 - TABLE_HEIGHT - TABLE_SHADOW_WIDTH / 2)
    drawShadow(table_shadow, screen)

    # Table Lines
    line.center = (300, CENTER_Y)
    pygame.draw.rect(screen, BLUE, line)
    line.centerx = WIDTH - 300
    pygame.draw.rect(screen, BLUE, line)

    # Net
    net.center = (CENTER_X, CENTER_Y + NET_HEIGHT)
    net_shadow.centerx = CENTER_X
    net_shadow.y = CENTER_Y - TABLE_WIDTH / 2
    pygame.draw.rect(screen, WHITE, net)
    pygame.draw.rect(screen, LIGHT_GRAY, net_shadow)

    # Scoreboard Background
    scoreboard.center = (CENTER_X, HEIGHT - SCOREBOARD_HEIGHT / 2)
    border.center = (CENTER_X, HEIGHT - (SCOREBOARD_HEIGHT + SCOREBOARD_BORDER) / 2)
    scoreboard_line.center = (CENTER_X, HEIGHT - SCOREBOARD_HEIGHT / 2)
    pygame.draw.rect(screen, BROWN, border)
    pygame.draw.rect(screen, ORANGE, scoreboard)
    pygame.draw.rect(screen, BROWN, scoreboard_line)
#end
