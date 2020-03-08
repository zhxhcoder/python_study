import turtle

turtle = turtle.Turtle()
screen = turtle.getscreen()


def main():
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    for i in range(50):
        turtle.forward(200)
        turtle.left(170)
    turtle.end_fill()
    screen.mainloop()


# 如果模块是被直接运行的，则代码块被运行，如果模块被import，则代码块不被运行。
if __name__ == "__main__":
    main()
