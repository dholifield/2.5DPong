import pygame
from pygame.locals import *
from constants import *
from shadow import drawShadow

# Paddle Object
class Paddle:
    # Preset data for paddles
    y = CENTER_Y
    z = 150
    speed = 0

    paddle = pygame.image.load('images/paddle.png')
    shadow = Rect(0,0, 8, 80)

    # Initialization of paddle
    def __init__(self, x):
        self.x = x
    #end

    # Resets the paddle position and speed
    def reset(self):
        self.speed = 0
        self.y = CENTER_Y
    #end

    # Renders the paddle to the screen
    def render(self, screen):
        self.shadow.center = (self.x, self.y - 150)
        drawShadow(self.shadow, screen)
        screen.blit(self.paddle, (self.x - 5, self.y + BALL_Z_START / 5 - 50))
    #end
#end Paddle

# Player Paddle Obejct
class playerPaddle(Paddle):
    # Initialization of paddle with keybinds
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

# Computer Paddle Object
class cpuPaddle(Paddle):
    # Initialization of paddle with difficulty
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
    #end

    # Updates the position and speed of the paddle
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
        #end
        self.y = self.y + self.speed
    #end
#end cpuPaddle
