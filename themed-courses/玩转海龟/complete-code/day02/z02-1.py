import turtle as t
t.bgpic('bg.gif')
t.setup(750, 750)
# 白色一环
t.penup()
t.goto(0, 300)
t.pendown()
t.color('black','white')
t.begin_fill()
t.circle(-300)
t.end_fill()
# 白色二环
t.penup()
t.goto(0, 270)
t.pendown()
t.color('black')
t.circle(-270)
# 黑色三环
t.penup()
t.goto(0, 240)
t.pendown()
t.color('black','black')
t.begin_fill()
t.circle(-240)
t.end_fill()
# 黑色四环
t.penup()
t.goto(0, 210)
t.pendown()
t.color('white')
t.circle(-210)

# 蓝色五环
t.penup()
t.goto(0, 180)
t.pendown()
t.color('black','blue')
t.begin_fill()
t.circle(-180)
t.end_fill()
# 蓝色六环
t.penup()
t.goto(0, 150)
t.pendown()
t.color('black')
t.circle(-150)
# 红色七环
t.penup()
t.goto(0, 120)
t.pendown()
t.color('black','red')
t.begin_fill()
t.circle(-120)
t.end_fill()
# 红色八环
t.penup()
t.goto(0, 90)
t.pendown()
t.color('black')
t.circle(-90)
# 黄色九环
t.penup()
t.goto(0, 60)
t.pendown()
t.color('black','yellow')
t.begin_fill()
t.circle(-60)
t.end_fill()
# 黄色十环
t.penup()
t.goto(0, 30)
t.pendown()
t.color('black')
t.circle(-30)

t.hideturtle()
t.done()