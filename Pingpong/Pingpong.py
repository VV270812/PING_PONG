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
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_a] and self.rect.x > 5:
           self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 595:
            self.rect.x += self.speed

    def fire(self):
        b1 = Bullet('b12.png', self.rect.centerx, self.rect.top, 10, 20, -15)
        bullets.add(b1)
    
sprite1 = Player('sprite1.png', 100, 400, 70, 80, 7)
sprite2 = Player('sprite1.png', 100, 400, 70, 80, 7)


finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        

    if finish != True:
        window.blit(background, (0, 0))
       

    display.update()
    clock.tick(60)