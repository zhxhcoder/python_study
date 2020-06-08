from turtle import *

color('red', 'pink')  # 画笔色red，背景色pink
begin_fill()
left(135)  # 左转135°
fd(100)  # 前进100像素
right(180)  # 画笔掉头

# 重点理解circle()
# 以垂直于当前方向的正左侧30像素处为圆心，圆心与当前位置的连线为半径,
# -180°方向（相对当前方向）画弧，画笔方向不变
# 如果是180°是画笔正向前进画弧，-180°时画笔是倒退着画弧的
circle(30, -180)

backward(35)  # 由于此时画笔方向约为绝对方向的135°，需倒退画线
right(90)
forward(35)
circle(-30, 180)
fd(100)
end_fill()
hideturtle()
done()
