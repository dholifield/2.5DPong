import pygame
from time import sleep, time
from random import seed, random
from pygame.locals import *
from constants import *
pygame.mixer.init()
miss_sound = pygame.mixer.Sound('sounds/hit_miss.wav')
paddle_sound = pygame.mixer.Sound('sounds/hit_table.wav')
table_sound = pygame.mixer.Sound('sounds/hit_miss.wav')

# Class for ping pong ball
class Ball:
    def __init__(self):
        self.ball = Rect((0,0),BALL_SIZE)
        self.shaddow = Rect(0,0, 15, 15)

        self.reset(1)
        self.ball.center = (self.x, self.y)
        self.count = 1
        seed(time)
    #end

    # Reset ball position
    def reset(self, player):
        self.x = BALL_X_START
        self.y = CENTER_Y
        self.z = BALL_Z_START
        self.sy = self.y

        self.x_speed = BALL_X_SPEED
        if player == 2:
            self.x = WIDTH - BALL_X_START
            self.x_speed = -BALL_X_SPEED
        self.y_speed = random() / 2 - 0.25
        self.z_speed = BALL_Z_START_SPEED
        self.z_accel = BALL_Z_ACCEL

        self.possession = player

        self.count = 250
    #end

    # Updates ball position
    def update(self):
        if self.count <= 0:
            self.z_speed = self.z_speed + self.z_accel
            self.z = self.z + self.z_speed
            if self.z <= 0:
                self.z = 0
                self.z_speed = BALL_Z_SPEED
                self.switchPossession()
                table_sound.play()

            self.x = self.x + self.x_speed
            self.y = self.y + self.y_speed

            diff_x = CENTER_X - self.x
            self.sy = self.y
            if abs(diff_x) > TABLE_LENGTH / 2:
                self.sy = self.sy - 150
        #end
        if self.count == 1:
            paddle_sound.play()
        elif self.count == 249:
            miss_sound.play()
    #end

    # Check paddle collisions for two paddle
    def paddles(self, paddle_one, paddle_two):
        self.paddleCollide(paddle_one)
        self.paddleCollide(paddle_two)
    #end

    # Alter x and y speeds of ball when in contact with a paddle
    def paddleCollide(self, paddle):
        x_diff = self.x - paddle.x
        if abs(x_diff) <= (PADDLE_WIDTH + self.ball.width) / 2:
            y_diff = self.y - paddle.y
            if abs(y_diff) <= (PADDLE_HEIGHT + self.ball.height) / 2:
                self.y_speed = self.y_speed + (y_diff / 50) - paddle.speed / 2
                self.x_speed = BALL_X_SPEED if x_diff > 0 else -BALL_X_SPEED
                paddle_sound.play()
    #end

    # Detects when the point is finished, points are awarded based on current possession
    def scored(self):
        scored = False
        # If ball falls of side of table
        if self.z < 5:
            diff = CENTER_Y - self.y
            if abs(diff) > (TABLE_WIDTH + self.ball.width) / 2:
                scored = True
        # If ball goes off back of table
        if self.x < 0 or self.x > WIDTH:
            scored = True
        return scored
    #end

    # Switch possession on contact with table
    def switchPossession(self):
        self.possession = 1 - self.possession + 2
    #end

    # Draws the shaddow of the ball
    def drawShaddow(self, screen):
        shape_surf = pygame.Surface(pygame.Rect(self.shaddow).size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, SHADDOW, shape_surf.get_rect())
        screen.blit(shape_surf, self.shaddow)
    #end

    # Renders the ball to the screen
    def render(self, screen):
        if self.count <= 0:
            self.ball.center = (self.x, self.y + (self.z) / 5)

            size = 20 - self.z / 25
            self.shaddow.size = (size, size)
            self.shaddow.center = (self.x, self.sy)
        else:
            self.count = self.count - 1
        if abs(CENTER_X - self.x) > TABLE_LENGTH / 2 or abs(CENTER_Y - self.y) < TABLE_WIDTH / 2:
            self.drawShaddow(screen)
            #pygame.draw.rect(screen, GRAY, self.shaddow)
        pygame.draw.rect(screen, WHITE, self.ball)
    #end
#end Ball
