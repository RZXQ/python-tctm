# 课堂练习4
# 将下方代码中的鼠标指针样式替换成图片genie.png
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 563))
bg = pygame.image.load('bg.jpg')
genie = pygame.image.load('genie.png')
# 鼠标指针显示设置
pygame.mouse.set_visible(False)
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.MOUSEMOTION:
            screen.blit(bg, (0, 0))
            x = e.pos[0]
            y = e.pos[1]
            screen.blit(genie, (x, y))
    pygame.display.update()
