# 课堂练习一
# 编写代码，使用turtle库为孙悟空绘制金箍棒
# 要求设置窗口标题为"齐天大圣"；设置窗口大小700*700；设置画笔粗细为15；隐藏小海龟
# 提示：
# 1. 金箍棒由三条线段组成，两端前进距离为100，中间前进距离为250
# 2. 金箍棒两端的颜色为金色gold，中间的颜色为红色red
# 3. 绘制金箍棒的起始位置坐标为(-200,-80)
import turtle

turtle.bgpic('bg1.gif')
# 在下方书写代码
turtle.title('齐天大圣')
turtle.setup(700, 700)
turtle.pensize(15)
turtle.hideturtle()
turtle.penup()
turtle.goto(-200, -80)
turtle.pendown()
turtle.pencolor('gold')
turtle.forward(100)
turtle.pencolor('red')
turtle.forward(250)
turtle.pencolor('gold')
turtle.forward(100)
turtle.done()
