from pygame import *

w = 1000
h = 600

window = display.set_mode((w,h))
display.set_caption('Лабиринт')
background = transform.scale(image.load('background.jpg'),(w,h))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < w - 80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < h - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, x2, y2, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.isLeft = True
        self.x1 = player_x
        self.y1 = player_y
        self.x2 = x2
        self.y2 = y2
    def update(self):
        if self.rect.x <= self.x1:
            self.isLeft = False
        if self.rect.x >= self.x2:
            self.isLeft = True
        if self.rect.y <= self.y1:
            self.up = False
        if self.rect.y >= self.y2:
            self.up = True

        if self.isLeft:
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        if self.isLeft:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

class Wall(sprite.Sprite):
    def __init__(self, col1, col2, col3, wall_x, wall_y, wall_w, wall_h):
        super().__init__()
        self.color = (col1, col2, col3)
        self.w = wall_w
        self.h = wall_h
        self.image = Surface((self.w, self.h))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


player = Player('hero.png',110, 30, 4)
monster1 = Enemy('cyborg.png',110, 110, 320, 320, 1)
monster2 = Enemy('cyborg.png',310, 230, 400, 420, 1)
final = GameSprite('treasure.png', w-120, 50, 0)

w1 = Wall(255, 0, 0,100,20,530,10)
w2 = Wall(255, 0, 0,100,20,10,80)
w3 = Wall(255, 0, 0,100,100,440,10)
w4 = Wall(255, 0, 0,100,90,10,290)
w5 = Wall(255, 0, 0,630,20,10,210)
w6 = Wall(255, 0, 0,230,220,400,10)
w7 = Wall(255, 0, 0,100,380,400,10)

font.init()
font = font.Font(None, 70)
win = font.render('You win at this game!', True, (255, 0, 255))
lose = font.render('You lose at this game', True, (255, 0, 255))

game = True
finish = False
clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load('Bones-Alize-_dizer.net_.ogg')
mixer.music.play()


while game:
    

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if not(finish):
        window.blit(background,(0,0))

        player.update()
        monster1.update()
        monster2.update()
        final.update()
            
        player.reset()
        monster1.reset()
        monster2.reset()
        final.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        if sprite.collide_rect(player,monster1) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6):
            finish = True
            window.blit(lose,(250,250))
        
        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (250,250))
    display.update()
    clock.tick(FPS)