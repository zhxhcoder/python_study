from turtle import *
from random import *

# 画树方法
def drawTree(n, l):
    pendown()
    pencolor('#5d3c3c')
    pensize( n / 1.5)
    forward(l)
    if n > 0:
        dr = randint(30, 40)
        dl =  randint(30, 40)
        move = l * (random() * 0.4 + 0.5)
        right(dr)
        drawTree(n - 1, move)
        left(dr + dl)
        drawTree(n - 1, move)
        right(dl)
    else:
        drawPetal(3)
    penup()
    backward(l)

# 花瓣位置生成
def petalPlace(m, x, y):
    penup()
    goto(x, y)
    pendown()
    setheading(0)
    tracer(False)
    for i in range(m):
        if i == 0:
            drawPetal(5)
        else:
            penup()
            goto(x, y)
            a = randint(20, 400)
            b = randint(-50, 50)
            forward(a)
            left(90)
            forward(b)
            right(90)
            pendown()
            drawPetal(5)

# 花朵绘画方法
def drawPetal(n):
    colormode(255)
    r = randint(200, 255)
    g = randint(8, 158)
    b = randint(8, 158)
    begin_fill()
    fillcolor(r, g, b)
    pencolor(r, g, b)
    circle(n)
    end_fill()

# 启动方法
def run():
    setup(1.0, 1.0)
    penup()
    goto(-50, -150)
    left(90)
    pendown()
    hideturtle()
    tracer(False)
    drawTree(13, 150)
    petalPlace(160, -100, -150)

run()
done()