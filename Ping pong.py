from pygame import*
from random import*
dx = -1
dy = -1

speedy = 5
speedx = 5
okno = display.set_mode((600,600))
class sharik(sprite.Sprite):
    def __init__(self, img, x, y):
        super().__init__()
        self.image = transform.scale(image.load(img), (50,50))
        #self.image = transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))
class platform1(sprite.Sprite):
    def __init__(self, img, x, y):
        super().__init__()
        self.image = transform.scale(image.load(img), (100,20))
        self.image = transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))
    def control(self):
        knopka = key.get_pressed()
        if knopka[K_UP] and self.rect.y > 0:
            self.rect.y -= 5
        if knopka[K_DOWN] and self.rect.y < 500:
            self.rect.y += 5
class platform(sprite.Sprite):
    def __init__(self, img, x, y):
        super().__init__()
        self.image = transform.scale(image.load(img), (100,20))
        self.image = transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))
    def control(self):
        knopka = key.get_pressed()
        if knopka[K_w] and self.rect.y > 0:
            self.rect.y -= 5
        if knopka[K_s] and self.rect.y < 500:
            self.rect.y += 5
b =sharik("qa.png",200,300)
a = platform("platform.png",10,10)
a2 = platform1("platform2.png",570,10)


game = True
clock = time.Clock()

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    okno.fill((250,250,0))
    b.ris()
    a.ris()
    a2.ris()
    a.control()
    a2.control()
    b.rect.x = b.rect.x +speedx*dx
    b.rect.y = b.rect.y +speedx*dy
    if sprite.collide_rect(a, b):
        dx *= -1
        speedx = randint(3,5)
        speedy = randint(3,5)
    if sprite.collide_rect(a2,b):
        dx *= -1
        speedx = randint(3,5)
        speedy = randint(3,5)
    if b.rect.y <= 0:
        dy *= -1
        speedx = randint(3,5)
        speedy = randint(3,5)
    if b.rect.y >= 550:
        dy *= -1
        speedx = randint(3,5)
        speedy = randint(3,5)
    display.update()
    clock.tick(40)