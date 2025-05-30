# 课堂练习三
# 编写代码实现，点击鼠标左键在夜空中印出星星的效果
# 提示：
# 1、设置窗口大小为700*350
# 2、turtle.shape()修改小海龟形状
# 3、turtle.addshape()添加小海龟形状
# 4、turtle.onscreenclick()监听鼠标点击事件
# 5、turtle.bgpic()用于设置背景图片
# 6、夜空图片（night.gif),星星图片（star.gif）
import turtle

turtle.setup(700, 350)
turtle.bgpic('night.gif')
image = 'star.gif'
turtle.addshape(image)
turtle.shape(image)


def draw(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.stamp()


turtle.onscreenclick(draw)
turtle.hideturtle()
turtle.done()
