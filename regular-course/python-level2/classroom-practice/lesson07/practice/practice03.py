# 课堂练习3
# 请在下列窗口中逐个显示文字“生日快乐”
# 要求：字体为'kaiti',字号为100,文字的坐标(190,390),每个字之间的间距100
# (苹果系统的字体可设置位：songti)
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 633))
bg = pygame.image.load('happy.png')
screen.blit(bg, (0, 0))
# 文字显示
list1 = '生日快乐'

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
