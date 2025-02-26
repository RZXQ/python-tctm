# 课堂练习四
# 目前在turtle窗口中有一个4行4列的棋盘，请根据以下提示计算这16个格子的中心点坐标并输出在控制台上
# 提示： 1.左上角第1个格子的坐标为(-240,240)
#       2.每个格子的宽为120，高为120
#       3.请结合本节课所学知识，利用循环嵌套计算这16个坐标

import turtle

turtle.setup(1200, 600)
turtle.bgpic('img/bg2.gif')

for i in range(4):
    cy = 240 - i * 120
    for j in range(4):
        cx = -240 + j * 120
        print('(', cx, ',', cy, ')')

turtle.done()
