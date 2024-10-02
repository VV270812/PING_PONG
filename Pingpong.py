from pygame import *
from random import randint
from time import time as tm
font.init()

window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('fon.jpg'), (700, 500))

clock = time.Clock()
game = True

mixer.init()

mixer.music.load('fon_music.mp3')
mixer.music.play()
mixer.music.set_volume(0.3)

font1 = font.SysFont('Arial', 70)
win2 = font1.render("Player 1 win!", True, (255, 215, 0))
lose = font1.render('Player 2 win!', True, (255, 215, 0))

font2 = font.SysFont('Arial', 36)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, w, h, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.h = h
        self.w = w

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <= 400:
            self.rect.y += self.speed
        
    
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <= 400:
            self.rect.y += self.speed

    
sprite1 = Player('sprite1.png', 630, 250, 50, 80, 7)
sprite2 = Player('sprite1.png', 5, 400, 50, 80, 7)

ball = GameSprite('mach.png', 350, 250, 50, 50, 7)

speed_x = 3
speed_y = 3
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    if finish != True:
        window.blit(background, (0, 0))
        sprite1.update_r()
        sprite1.reset()
        sprite2.update_l()
        sprite2.reset()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if ball.rect.y > 450 or ball.rect.y < 0:
       speed_y *= -1
    
    if sprite.collide_rect(sprite1, ball) or sprite.collide_rect(sprite2, ball):
        speed_x *= -1
       

    display.update()
    clock.tick(60)
