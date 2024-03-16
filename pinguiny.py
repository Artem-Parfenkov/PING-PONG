from pygame import *
from random import *
from time import time as tm
window = display.set_mode((700,500))
display.set_caption('SUSLIK')
background = transform.scale(image.load('xz.jpeg'),(700,500))
clock = time.Clock()
finish = False
game = True
class GaveSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
       sprite.Sprite.__init__(self)
       self.image = transform.scale(image.load(player_image),(size_x,size_y)) 
       self.speed = player_speed
       self.rect =self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GaveSprite):
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5 :
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5 :
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed


ball = GaveSprite('bfrg.png',350,250,50,50,1)   
crosh_l = Player('kekich.png',600,400,70,100,10)
crosh_r = Player('kekich.png',30,400,70,100,10)

speedx = 1
speedy = 1


font.init()
font1 = font.SysFont('Arial',30)
win = font1.render('be positiv',True,(255,0,255))
lose = font1.render('you lose',True,(255, 0, 255))


while game:
    for e in event.get():

        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0,0))

        ball.rect.x += speedx
        ball.rect.y += speedy

        crosh_l.update_left()
        crosh_r.update_right()
        if ball.rect.y <= 0 :
            speedy *= -1
        if ball.rect.y >= 450:
            speedy *= -1

        crosh_l.reset()
        crosh_r.reset()
        ball.reset()
        
    display.update()
    clock.tick(60)