# 课堂练习四
# 已知turtle窗口中有三个按钮，请编写代码实现点击第一个按钮时绘制正方形、点击第二个按钮绘制矩形、点击第三个按钮绘制圆形的效果
# 要求在绘制新图形时，清除之前绘制的图形
# 提示：
# （1）第一个按钮的点击区域范围是-279 < x < -137 ， 111 < y < 175
#     第二个按钮的点击区域范围是-70 < x < 74 ， 111 < y < 175
#     第三个按钮的点击区域范围是141 < x < 285， 111 < y < 175
# （2）绘制正方形和矩形的起始位置是(-95, 29)，绘制圆形的起始位置是(5, -138)
# （3）正方形的边长为200，长方形的宽高为200*150，圆形的半径为100
# （4）将绘制形状的代码定义在draw函数中
# （5）在点击事件中调用draw函数
import turtle

turtle.bgpic('bg.gif')
turtle.setup(679, 488)
turtle.hideturtle()
turtle.pensize(5)


# 请在下方书写代码
def draw(x, y):
    print(x, y)
    turtle.clear()
    turtle.penup()
    turtle.goto(-95, 29)
    turtle.pendown()
    if -279 < x < -137 and 111 < y < 175:
        i = 1
        while i <= 4:
            turtle.forward(200)
            turtle.right(90)
            i = i + 1
    elif -70 < x < 74 and 111 < y < 175:
        i = 1
        while i <= 2:
            turtle.forward(200)
            turtle.right(90)
            turtle.forward(150)
            turtle.right(90)
            i = i + 1
    elif 141 < x < 285 and 111 < y < 175:
        turtle.penup()
        turtle.goto(5, -138)
        turtle.pendown()
        turtle.circle(100)


turtle.onscreenclick(draw)
turtle.done()
