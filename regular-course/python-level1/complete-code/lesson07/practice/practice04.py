# 课堂练习4
# 请编写程序，判断当在输入框中输入密码3579时，就在背图中的密码框中绘制密码文字3579，否则就在控制台输出密码错误
# 提示：
# 使用input()输入密码'3579'
# 使用if语句判断输入的密码是否是3579
# 满足if语句，就在密码框中使用write()绘制文字密码'3579'，否则在控制台输出密码错误
# 绘制文字的起始位置是(30,-187)
# 字体为"arial"，字号22
import turtle

turtle.bgpic('bg04.gif')
# 在下方编写代码
password = input('请输入密码：')
if password == '3579':
    turtle.penup()
    turtle.goto(30, -187)
    turtle.pendown()
    turtle.write(password, font=('arial', 22))
else:
    print('密码错误')

turtle.hideturtle()
turtle.done()
