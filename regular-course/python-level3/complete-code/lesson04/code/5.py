import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1100, 600))
bg = pygame.image.load("images/bg.png")


class FlyObject:
    def __init__(self, img, x, y):
        self.img = pygame.image.load(img)
        w, h = self.img.get_size()
        self.centerX = x + w / 2
        self.centerY = y + h / 2
        self.speedY = random.randint(30, 48)
        self.speedX = random.randint(-10, 10)
        self.angle = 0
        self.imgParted = pygame.image.load(img.replace('full.png', 'parted.png'))
        typeName = type(self).__name__
        self.music = pygame.mixer.Sound('music/' + typeName + '.mp3')
        self.isCut = False

    def draw(self):
        if self.speedX < 0:
            self.angle -= 5
        else:
            self.angle += 5
        self.newImg = pygame.transform.rotate(self.img, self.angle)
        self.rect = self.newImg.get_rect(center=(self.centerX, self.centerY))
        screen.blit(self.newImg, self.rect)

    def move(self):
        self.centerY -= self.speedY
        self.speedY -= 2
        self.centerX -= self.speedX

    def bang(self):
        self.img = self.imgParted
        self.music.play()


class Fruit(FlyObject):
    pass


fruitImgs = ['images/pineapple/full.png', 'images/orange/full.png',
             'images/pitaya/full.png', 'images/kiwi/full.png',
             'images/lemon/full.png', 'images/apple/full.png',
             'images/pomegranate/full.png', 'images/peach/full.png',
             'images/watermelon/full.png', 'images/banana/full.png',
             'images/coconut/full.png']
fruits = []
for i in range(10):
    fruit = Fruit(random.choice(fruitImgs), random.randint(100, 900), 600)
    fruits.append(fruit)


class Bomb(FlyObject):
    pass


bomb = Bomb('images/bomb/full.png', random.randint(100, 900), 600)


class Knife:
    def __init__(self, img, x, y):
        self.img = pygame.image.load(img)
        self.x = x
        self.y = y

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

    def move(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        self.x = mouseX - 60
        self.y = mouseY - 60

    def collide(self, fruit):
        if fruit.isCut:
            return
        knifeMask = pygame.mask.from_surface(self.img)
        fruitMask = pygame.mask.from_surface(fruit.newImg)
        offset = (fruit.rect.x - self.x, fruit.rect.y - self.y)
        result = knifeMask.overlap(fruitMask, offset)
        if result:
            fruit.bang()
            fruit.isCut = True


knife = Knife('images/knife.png', 550, 300)

while True:
    screen.blit(bg, (0, 0))
    for fruit in fruits:
        fruit.draw()
        fruit.move()
        knife.collide(fruit)
        # 1. 判断每个水果的中心点坐标centerY是否大于700
        if fruit.centerY > 700:
            # 2. 如果大于700，就获取移出界面的水果的索引
            i = fruits.index(fruit)
            # 3. 将该水果对象替换为新创建的水果对象
            fruits[i] = Fruit(
                random.choice(fruitImgs),
                random.randint(100, 900), 600
            )
    bomb.draw()
    bomb.move()
    knife.collide(bomb)
    knife.draw()
    knife.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    pygame.time.delay(80)
