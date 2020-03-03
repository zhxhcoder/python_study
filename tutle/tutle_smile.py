from turtle import *

screensize(600, 600)
speed(10)


def Arc(initial_degree, step, rotate, rangeNum):
    seth(initial_degree)
    for i in range(rangeNum):
        fd(step)
        lt(rotate)


def Line(x, y, delta_x, delta_y):
    pu()
    goto(x, y)
    pd()
    goto(x + delta_x, y + delta_y)


# 笑脸的小圆脸
pensize(15)
color('#DA993B', '#FDE492')
pu()
goto(0, -200)
pd()
begin_fill()
circle(200, 366)
end_fill()

# 腮红
# 左侧
seth(90)
color('#FFE4E1')
pu()
goto(-90, -15)
pd()
begin_fill()
circle(42)
end_fill()
# 左羞羞
color('#FFB6C1')
Line(-125, 0, -15, -30)
Line(-150, 0, -15, -30)

# 右侧
color('#FFE4E1')
pu()
goto(90, -15)
pd()
begin_fill()
circle(-42)
end_fill()
# 右羞羞
color('#FFB6C1')
Line(140, 0, -15, -30)
Line(165, 0, -15, -30)

# 笑脸的眼睛
pensize(15)
# 左眼
color('#834F20')
pu()
goto(-48, 50)
pd()
pensize(15)
Arc(100, 1, 2, 10)
Arc(140, 0.75, 0.75, 110)
Arc(-125, 1, 2, 10)

# 右眼
pu()
goto(48, 50)
pd()
pensize(15)
Arc(80, 1, -2, 10)
Arc(40, 0.75, -0.75, 110)
Arc(-55, 1, -2, 10)

# 笑脸的嘴巴
pensize(10)
pu()
# goto(-55,-80)
pd()
color('#B5501A')
# 微笑弧
# Arc(-85,0.75,0.8,212)#Arc(-85,0.45,0.5,340)


# 两瓣嘴
pu()
goto(-77, -80)
pd()
Arc(-85, 0.6, 1, 170)
Arc(-85, 0.6, 1, 180)

hideturtle()
done()
