# 课堂练习2
# 请使用海龟绘图的相关指令为坐标系添加东西南北四个方位文字
# 提示：
# 使用turtle.write()在坐标系添加东西南北方位
# 字体为"arial"，字号20，加粗"bold"
# 方位"北"在坐标（0，220）
# 方位"南"在坐标（0，-260）
# 方位"东"在坐标（240，20）
# 方位"西"在坐标（-290，20）
# 隐藏小海龟
import turtle

turtle.bgpic('bg02.gif')
# 在下方编写代码
turtle.penup()
turtle.goto(0, 220)
turtle.pendown()
turtle.write('北', font=('arial', 20, 'bold'))

turtle.penup()
turtle.goto(0, -260)
turtle.pendown()
turtle.write('南', font=('arial', 20, 'bold'))

turtle.penup()
turtle.goto(240, 20)
turtle.pendown()
turtle.write('东', font=('arial', 20, 'bold'))

turtle.penup()
turtle.goto(-290, 20)
turtle.pendown()
turtle.write('西', font=('arial', 20, 'bold'))
turtle.hideturtle()
turtle.done()
