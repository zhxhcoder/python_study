# -*- coding: utf-8 -*-
import random
from time import clock
from turtle import Turtle


def tree(plist, l, a, f):
    """
    plist 是turtle箭头的列表
    l 是初始树枝的长度
    a 是两根树枝之间夹角的一半
    f 是每层树枝之间长度的因数.
    """
    r = random.randint(2, 3)
    if l > 3:
        lst = []
        for p in plist:
            if l < 50:
                p.color(34, int(200 - 3 * l), 34)
                p.pensize(3)
            p.forward(l)
            # 沿当前方向前进l
            q = p.clone()
            # 创建一个副本
            if (r == 3):
                m = p.clone()
                m.left(random.randint(-5, 5))
                lst.append(m)
            p.left(a + random.randint(-10, 10))
            # 原本左转a度
            q.right(a + random.randint(-10, 10))
            # 副本右转a度
            lst.append(p)
            lst.append(q)
            # 将p,q分别加到列表后
        for x in tree(lst, l * f, a, f):
            yield None


def maketree(l, a, f, x, y):
    '''这个函数用来初始化箭头的参数
    l 是初始树枝的长度
    a 是两根树枝之间夹角的一半
    f 是每层树枝之间长度的因数
    x和y是树根位置,(0,0)在屏幕中心
    '''
    p = Turtle()
    # 创建一个Turtle类的对象
    p.getscreen().colormode(255)
    # 获得屏幕句柄，可以对其进行操作
    # 颜色模式改为255，可以使用RGB颜色
    p.pencolor(139, 69, 19)
    # p.color('brown')
    # Turtle的颜色为棕色
    p.pensize(6)
    # 笔的大小为6
    p.setundobuffer(None)
    # 不设置撤销缓冲区
    p.hideturtle()
    # 隐藏箭头
    p.speed(0)
    # 设置速度，0-10，0是最快的
    p.getscreen().tracer(5000, 0)
    # 获得屏幕句柄，可以对其进行操作
    # 每5000次操作将屏幕刷新，延时为0
    p.left(90)
    # 将Turtle的前进方向左转90度，使方向竖直向上
    p.penup()
    # 把笔抬起来
    p.goto(x, y)
    # p.forward(-210)
    # 笔向前移动-210个单位（向后移动210个像素）
    p.pendown()
    # 把笔放下
    # 这三条语句是一个组合相当于先把笔收起来再移动到指定位置，再把笔放下开始画
    # 否则turtle一移动就会自动的把线画出来
    t = tree([p], l, a, f)
    for x in t:
        pass
    # print(len(p.getscreen().turtles()))
    # 输出箭头总数


def main():
    a = clock()
    maketree(100, 35, 0.6375, -100, -210)
    maketree(110, 60, 0.67, -400, -100)
    maketree(120, 30, 0.6, 500, -160)
    maketree(145, 45, 0.65, 150, -80)
    b = clock()
    return "done: %.2f sec." % (b - a)


if __name__ == "__main__":
    msg = main()
    print(msg)
    tuple.mainloop()
    # 确保不会自动退出
