import turtle as t


def hair():
    t.penup()
    t.goto(-50, 150)
    t.pendown()
    t.fillcolor('#a2774d')
    t.begin_fill()
    for j in range(10):
        t.setheading(60 - (j * 36))
        t.circle(-50, 120)
    t.end_fill()


def face():
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.fillcolor('#f2ae20')
    t.begin_fill()
    t.setheading(180)
    t.circle(85)
    t.end_fill()
    # 下巴
    t.circle(85, 120)
    t.fillcolor('white')
    t.begin_fill()
    t.circle(85, 120)
    t.setheading(135)
    t.circle(100, 95)
    t.end_fill()


def ears(dir):
    t.penup()
    t.goto((0 - dir) * 30, 90)
    t.setheading(90)
    t.pendown()
    t.fillcolor('#f2ae20')
    t.begin_fill()
    t.circle(dir * 30)
    t.end_fill()

    t.penup()
    t.goto((0 - dir) * 40, 85)
    t.setheading(90)
    t.pendown()
    t.fillcolor('white')
    t.begin_fill()
    t.circle(dir * 17)
    t.end_fill()


def nose():
    t.penup()
    t.goto(20, 0)
    t.setheading(90)
    t.pendown()
    t.fillcolor('#a2774d')
    t.begin_fill()
    t.circle(20)
    t.end_fill()


def eye(dir):
    t.penup()
    t.goto((0 - dir) * 30, 20)
    t.setheading(0)
    t.pendown()
    t.fillcolor('black')
    t.begin_fill()
    t.circle(10)
    t.end_fill()


def mouth():
    t.penup()
    t.goto(0, 0)
    t.setheading(-90)
    t.pendown()
    t.forward(50)
    t.setheading(0)
    t.circle(80, 30)
    t.penup()
    t.goto(0, -50)
    t.setheading(180)
    t.pendown()
    t.circle(-80, 30)


hair()
ears(1)
ears(-1)
face()
eye(1)
eye(-1)
mouth()
nose()
t.done()