from pygame import *

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
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5: # вниз
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 620: # наверх
            self.rect.y += speed 

    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5: # вниз
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 620: # наверх
            self.rect.y += speed 

back = (200, 255, 255)
window = display.set_mode((600,500))
window.fill(back)

game = True
finish = False
clock = clock.Clock()

# 1 мяч, 2 палки
racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tennis_ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render( '1 ИГРОК ЛОХ', True, (180, 0, 0))
lose2 = font.render( '2 ИГРОК ЛОХ', True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill()
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    closk.tick(60)
