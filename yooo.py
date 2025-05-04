from pygame import *
from random import randint

font.init()
font1 = font.Font(None, 80)
win1 = font1.render('Player1 win', True, (255, 0, 255))
win2 = font1.render('Player2 win', True, (255, 0, 255))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def updatel(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def updater(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_width - 80:
            self.rect.y += self.speed


racket1 = Player('racket.png', 30, 200, 4, 50, 8)
racket2 = Player('racket.png', 470, 200, 4, 50, 8)
ball = GameSprite('tenis_ball.png', 250, 250, 50, 50, 718)




win_width = 500
win_height = 500
display.set_caption("Ping-pong")
window = display.set_mode((win_width, win_height))
back = (255, 255, 255)
window.fill(back)

finish = False
run = True


speed_x = 4
speed_y = 4 





while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        window.fill(back)
        racket1.updatel()
        racket2.updater()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):                                         
            speed_x *= -1   

        if ball.rect.y > 450 or ball.rect.y <0:                                         
            speed_y *= -1  

        if ball.rect.x <-50:             
            finish = True                            
            window.blit(win1, (150, 250))
     

        if ball.rect.x > win_width:
            finish = True
            window.blit(win2, (150, 250))
      

        ball.reset()                                         
        racket1.reset()                                         
        racket2.reset()                                         

    display.update()                                         
    time.delay(50)                                         