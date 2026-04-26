from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite): # класс ракетки
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed

back = (200, 255, 255)
window = display.set_mode((600, 500))
display.set_caption('Пинг-понг')
window.fill(back)

game = True
clock = time.Clock()
FPS = 60

racket1 = Player('Coin.png', 30, 200, 4, 50, 150) # создание ракеток и мяча
racket2 = Player('Coin.png', 520, 200, 4, 50, 150)
ball = GameSprite('Heart.png', 275, 225, 4, 50, 50)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill(back)
    racket1.update_l()
    racket2.update_r()
    racket1.reset()
    racket2.reset()
    ball.reset()

    display.update()
    clock.tick(FPS)
