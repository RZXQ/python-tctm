import turtle

turtle.bgpic('files/bg.gif')
words = ['eye', 'book', 'face', 'leg', 'foot', 'cat', 'dog', 'apple', 'bus', 'man']
turtle.hideturtle()


def create_words(content):
    temp = content[1:len(content) - 1]
    temp_words = temp.split(',')
    new_words = []
    for i in temp_words:
        if temp_words.index(i) == 0:
            new_words.append(i[1:len(i) - 1])
        else:
            new_words.append(i[2:len(i) - 1])
    return new_words


def show():
    turtle.clear()
    x = - 280
    y = 150
    for w in words:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.write(w, font=('arial', 20, 'bold'))
        y = y - 50
        if y < -200:
            y = 150
            x = x + 160


show()


def click(x, y):
    if 115 <= x <= 240 and 210 <= y <= 270:
        mode = turtle.textinput('排序', '方式：升序/降序')
        if mode == '升序':
            words.sort()
        elif mode == '降序':
            words.sort(reverse=True)
        show()
    elif 255 <= x <= 380 and 210 <= y <= 270:
        name = turtle.textinput('添加', '单词的名称')
        words.append(name)
        show()
    elif 395 <= x <= 520 and 210 <= y <= 270:
        name = turtle.textinput('删除', '单词的名称')
        words.remove(name)
        show()


turtle.onscreenclick(click)
turtle.done()
