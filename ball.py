import pygame
from time import sleep, time
from random import seed, random
from pygame.locals import *
from constants import *
from shadow import drawShadow
pygame.mixer.init()
miss_sound = pygame.mixer.Sound('sounds/hit_miss.wav')
paddle_sound = pygame.mixer.Sound('sounds/hit_table.wav')
table_sound = pygame.mixer.Sound('sounds/hit_miss.wav')

# Ball Object
class Ball:
    # Preset values for a ball
    ball = Rect((0,0),BALL_SIZE)
    shadow = Rect(0,0, 15, 15)

    x = BALL_X_START
    y = CENTER_Y

    ball.center = (x, y)
    count = 1
    seed(time)

    # Initialization of ball
    def __init__(self):
        self.reset(1)
    #end

    # Reset ball position and speed
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

        # Play sound if ball is hit or missed
        if self.count == 1:
            paddle_sound.play()
        elif self.count == 249:
            miss_sound.play()
    #end

    # Alter x and y speeds of ball when in contact with a paddle
    def paddleCollide(self, paddles):
        for paddle in paddles:
            x_diff = self.x - paddle.x
            if abs(x_diff) <= (PADDLE_WIDTH + self.ball.width) / 2:
                y_diff = self.y - paddle.y
                if abs(y_diff) <= (PADDLE_HEIGHT + self.ball.height) / 2:
                    self.y_speed = self.y_speed + (y_diff / 50) - paddle.speed / 2
                    self.x_speed = BALL_X_SPEED if x_diff > 0 else -BALL_X_SPEED
                    paddle_sound.play()
                #end
            #end
        #end
    #end

    # Detects when a point is scored
    def scored(self):
        scored = False
        # If ball falls off side of table
        if self.z < BALL_Z_SPEED:
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

    # Renders the ball to the screen
    def render(self, screen):
        if self.count <= 0:
            self.ball.center = (self.x, self.y + (self.z) / 5)

            size = 20 - self.z / 25
            self.shadow.size = (size, size)
            self.shadow.center = (self.x, self.sy)
        else:
            self.count = self.count - 1
        if abs(CENTER_X - self.x) > TABLE_LENGTH / 2 or abs(CENTER_Y - self.y) < TABLE_WIDTH / 2:
            drawShadow(self.shadow, screen)
        pygame.draw.rect(screen, WHITE, self.ball)
    #end
#end Ball
