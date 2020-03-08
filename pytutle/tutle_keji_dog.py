from turtle import *

pensize(5)
speed(0)
##color('#F4A460')#橘黄
##color('#FFE4E1')#肉粉

##【背景圆】
color('#B088FF')  # 浅紫
pu()
goto(0, -200)
pd()
begin_fill()
circle(200)
end_fill()


##定义画弧函数
def Arc(initial_degree, range_num, step, rotate_degree):
    seth(initial_degree)
    for n in range(range_num):
        fd(step)
        rt(rotate_degree)  #


##定义填充矩形函数
def Rect(x, y, height, width):
    pu()
    goto(x, y)
    pd()
    begin_fill()
    goto(x + width, y)
    goto(x + width, y + height)
    goto(x, y + height)
    goto(x, y)
    end_fill()


##定义绘制填充等边三角形函数
def Triangle(x, y, side_length):  # 等边三角形底边左角
    pu()
    goto(x, y)
    pd()
    begin_fill()
    seth(0)
    fd(side_length)
    rt(120)  # lt()是正立三角形
    fd(side_length)
    rt(120)  # lt()是正立三角形
    fd(side_length)
    end_fill()


# 中轴线——辅助绘图线
# color("green")
# Rect(-200,0,1,400)#x轴
# Rect(0,-200,400,1)#y轴

##【图层1——面部轮廓】
color('#F4A460')  # 橘黄
# 左耳
pu()
goto(-83.13, -10.94)
pd()
begin_fill()

Arc(120, 145, 1, 1 / 4)
goto(-30, 50)
end_fill()

# 右耳
pu()
goto(83.13, -10.94)  # (88.13,10.94)
pd()
begin_fill()
Arc(60, 145, 1, -1 / 4)
goto(30, 50)
end_fill()

# 腮帮
# 右腮帮
pu()
goto(83.13, -10.94)  # 0
pd()
begin_fill()
Arc(-35, 135, 1, 9 / 11)  # 1
# print(pos())

# 下巴
# pencolor("yellow")
Arc(-145, 70, 1, 3 / 10)  # 右半下颌2
# print(pos())

# pencolor("red")
Arc(-175, 40, 1, 1 / 5)  # 下巴连接线3
# print(pos())

# pencolor("pink")
Arc(168, 70, 1, 3 / 10)  # 左半下颌4
# print(pos())

# 左腮帮
# pencolor("grey")
Arc(146, 135, 1, 9 / 11)  # 5
# print(pos())

# 两耳连接
pu()
goto(-30, 50)
Arc(15, 80, 1, 1 / 2)

end_fill()

##【图层2——耳部轮廓】
color('pink')  # FFC0CB
# 左耳
pu()
goto(-42, 50)
pd()
begin_fill()
Arc(-164, 55, 1, -7 / 8)
Arc(120, 100, 1, 1 / 3)
goto(-42, 50)
end_fill()

# 右耳
pu()
goto(42, 50)
pd()
begin_fill()
Arc(-16, 55, 1, 7 / 8)  # (81.13,15.94)
# print(pos())
Arc(60, 100, 1, -1 / 3)  # (104.15,111.82)
# print(pos())
goto(42, 50)
end_fill()

##【图层3——眼部轮廓】
# 左黑眼豆豆
pu()
goto(-46, -8)
pd()
color("black")
seth(180)
len = 0.3
begin_fill()
for k in range(2):  # 双弧绘制椭圆
    for j in range(60):
        if j < 30:
            len += 0.04
        else:
            len -= 0.04

        fd(len)
        lt(3)
end_fill()
# 左眼白光
color("white")
Rect(-43, -38, 6, 2)

# 右黑眼豆豆
pu()
goto(46, -8)
pd()
color("black")
seth(180)
len = 0.3
begin_fill()
for k in range(2):  # 将相同的动作重复做一遍
    for j in range(60):
        if j < 30:
            len += 0.04
        else:
            len -= 0.04

        fd(len)
        lt(3)
end_fill()
# 右眼白光
color("white")
Rect(40, -38, 6, 2)

##【图层4——白鼻子轮廓】
pu()
goto(10, 50)
pd()
goto(-10, 50)
color("white")
begin_fill()
Arc(-82, 140, 1, 1 / 7)  # 结束角度A=-82-140*1/7=-102
Arc(-112, 20, 1.1, -1.2)  # 结束角度B=-112+20*1.2=-88
# setx(-xcor())
goto(-xcor(), ycor())
seth
Arc(88, 20, 1.1, -1.2)  # 求A的y轴对称角度
Arc(102, 140, 1, 1 / 7)  # 求8的y轴对称角度
goto(10, 50)
end_fill()
pd()

# 圆嘴
pu()
goto(0, -150)
seth(0)
pd()
begin_fill()
circle(35)
end_fill()

# 黑鼻头
color("black")
Triangle(-10, -120, 20)

end_fill()

hideturtle()
done()
