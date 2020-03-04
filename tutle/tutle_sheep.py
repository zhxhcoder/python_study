# -*- coding:utf-8 -*-
# __author__ :kusy
# __content__:文件说明
# __date__:2018/8/21 13:08
import turtle
import time
import math as m


class Sheep(object):

    def __init__(self,xsize):
        self.t = turtle.Turtle()
        self.xsize = xsize
        t = self.t
        # 画笔设置
        t.screen.screensize(canvwidth=1000,canvheight=500,bg='white')
        t.pensize(2)
        t.speed(10)
        # t.hideturtle()
        #初始化画笔位置
        t.penup()
        t.setpos(self.xsize,0)
        t.pendown()

    # 设置画笔坐标
    def setxy(self,x,y):
        t = self.t
        t.penup()
        pos_x = t.position()[0]
        pos_y = t.position()[1]
        t.setpos(pos_x + x,pos_y + y)
        t.pendown()

    def create_sheep(self):
        t = self.t
        # 羊头
        self.setxy(-200,0)
        t.fillcolor('black')
        t.begin_fill()
        t.circle(100)
        t.end_fill()

        # 眼睛
        # 眼白
        print(t.position())
        self.setxy(-20,120)

        t.fillcolor('white')
        t.begin_fill()
        t.seth(45)
        t.circle(18,-280)
        t.seth(45)
        t.circle(-20,292)
        t.end_fill()
        # 眼珠
        self.setxy(3,12)
        t.fillcolor('black')
        t.begin_fill()
        t.seth(85)
        t.circle(10)
        t.seth(85)
        t.circle(-10)
        t.end_fill()
        # 眼心
        t.fillcolor('white')
        t.begin_fill()
        t.seth(85)
        t.circle(3)
        t.seth(85)
        t.circle(-3)
        t.end_fill()

        # 嘴
        self.setxy(0,-100)
        t.color('red')
        t.seth(300)
        t.forward(8)
        self.setxy(-1, 3)
        t.seth(0)
        t.circle(80,60)
        self.setxy(2, -2)
        t.seth(145)
        t.forward(8)
        t.color('black')

        # 耳朵
        self.setxy(-145,120)
        p1 = t.position()
        t.fillcolor('black')
        t.begin_fill()
        t.seth(0)
        t.circle(-120,20)
        p2 = t.position()
        t.setpos(p1)
        t.seth(60)
        t.circle(-30,120)
        t.goto(p2)
        t.end_fill()

        # 身体
        self.setxy(41,12)
        t.seth(45)
        t.circle(-150,100)
        t.pensize(5)
        t.seth(0)
        t.circle(-120,30)
        t.seth(60)
        t.circle(-15,320)
        t.seth(330)
        t.circle(-80,180)
        t.seth(210)
        t.circle(-80,90)

        #4条腿
        t.pensize(2)
        for leg in range(4):
            self.setxy(8+15*leg,0)
            t.seth(270)
            t.forward(80)
            t.seth(0)
            t.forward(8)
            t.seth(90)
            t.forward(80)

        #草
        self.setxy(-200,-80)
        p3 = t.position()
        t.color('green')
        t.fillcolor('green')
        t.begin_fill()
        t.seth(120)
        t.forward(30)
        t.seth(330)
        t.forward(30)
        t.seth(60)
        t.forward(40)
        t.seth(260)
        t.forward(45)
        t.setpos(p3)
        t.end_fill()

if __name__ == '__main__':
    for x in (0,350):
        sheep = Sheep(x)
        sheep.create_sheep()
    time.sleep(5)