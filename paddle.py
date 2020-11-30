import pygame
from pygame.locals import *
from constants import *

class Paddle:
    def __init__(self, x):
        self.x = x
        self.y = CENTER_Y
        self.z = 150
        self.speed = 0

        #self.paddle = Rect(0,0, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.paddle = pygame.image.load('paddle.png')
        self.shaddow = Rect(0,0, 8, 80)
    #end

    # Resets the paddle position and speed
    def reset(self):
        self.speed = 0
        self.y = CENTER_Y
    #end

    # Draws the shaddow of the paddle
    def drawShaddow(self, screen):
        shape_surf = pygame.Surface(pygame.Rect(self.shaddow).size, pygame.SRCALPHA)
        pygame.draw.rect(shape_surf, SHADDOW, shape_surf.get_rect())
        screen.blit(shape_surf, self.shaddow)
    #end

    # Renders the paddle to the screen
    def render(self, screen):
        #self.paddle.center = (self.x, self.y + BALL_Z_START / 5)
        #pygame.draw.rect(screen, WHITE, self.paddle)
        self.shaddow.center = (self.x, self.y - 150)
        self.drawShaddow(screen)
        screen.blit(self.paddle, (self.x - 5, self.y + BALL_Z_START / 5 - 50))
    #end
#end Paddle


class playerPaddle(Paddle):
    def __init__(self, x, up_key, down_key):
        super().__init__(x)
        self.up_key = up_key
        self.down_key = down_key
    #end

    # Updates the position and speed of the paddle
    def update(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[self.up_key] and self.y < PADDLE_MAX:
            if self.speed < 0:
                self.speed = 0;
            if self.speed < PADDLE_SPEED:
                self.speed = self.speed + PADDLE_ACCEL
        elif pressed_key[self.down_key] and self.y > PADDLE_MIN:
            if self.speed > 0:
                self.speed = 0;
            if self.speed > -PADDLE_SPEED:
                self.speed = self.speed - PADDLE_ACCEL
        else:
            if abs(self.speed) >= 0.1:
                self.speed = self.speed - (abs(self.speed) / self.speed) * PADDLE_DECEL
            else:
                self.speed = 0
        self.y = self.y + self.speed

    #end
#end playerPaddle


class cpuPaddle(Paddle):
    def __init__(self, x, ball, difficulty):
        super().__init__(x)
        self.ball = ball
        self.difficulty = difficulty

        if difficulty == 1:
            self.max_speed = 1
            self.accel = 0.01
            self.decel = 0.03
        elif difficulty == 2:
            self.max_speed = 1.5
            self.accel = 0.02
            self.decel = 0.10
        elif difficulty == 3:
            # Expert difficulty
            pass
    #end

    def update(self):
        diff = self.y - self.ball.y
        direction = self.ball.x_speed * (self.x - self.ball.x)
        if direction > 0 and self.ball.count == 0:
            if diff < 0:
                if self.speed < 0 and self.difficulty > 2:
                    self.speed = 0;
                if self.speed < self.max_speed:
                    self.speed = self.speed + self.accel
            elif diff > 0:
                if self.speed > 0 and self.difficulty > 2:
                    self.speed = 0;
                if self.speed > -self.max_speed:
                    self.speed = self.speed - self.accel
            else:
                if abs(self.speed) >= 0.1:
                    self.speed = self.speed - (abs(self.speed) / self.speed) * self.decel
                else:
                    self.speed = 0
        else:
            if abs(self.speed) >= 0.1:
                self.speed = self.speed - (abs(self.speed) / self.speed) * self.decel
            else:
                self.speed = 0
        self.y = self.y + self.speed
    #end
#end cpuPaddle
