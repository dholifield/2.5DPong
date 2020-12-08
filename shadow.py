import pygame
from pygame.locals import *
from constants import *

# Draws the shadow of the ball
def drawShadow(shadow, screen):
    shape_surf = pygame.Surface(pygame.Rect(shadow).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, SHADOW, shape_surf.get_rect())
    screen.blit(shape_surf, shadow)
#end
