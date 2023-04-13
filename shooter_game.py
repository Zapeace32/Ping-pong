from pygame import *
from random import randint


class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed

win_height = 1000
win_width = 1000
window = display.set_mode((win_width, win_height))
display.set_caption("Ping-pong")
fon = (105,102,216)
window.fill(fon)

platform1 = Player('racket.png',50,200,15,100,150)
platform2 = Player('racket.png',770,200,15,100,150)
game = True
finish = False
clock = time.Clock()
FPS = 60
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill(fon)
        platform1.update_l()
        platform2.update_r()
        
        
        platform1.reset()
        platform2.reset()




    
        
    display.update()
    clock.tick(FPS)