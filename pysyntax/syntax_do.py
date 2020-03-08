print("######################################for - else######################################")
for i in [1, 2, 3, 4]:
    print(i)
else:
    print(i, '我是else')

for i in [1, 2, 3, 4]:
    if i > 2:
        print(i)
        break
else:
    print(i, '我是else')
print("######################################一颗星(*)和两颗星(**)######################################")


def multi_sum(*args):
    s = 0
    for item in args:
        s += item
    return s


print(multi_sum(3, 4, 5))


# Python 函数允许同时全部或部分使用固定参数、默认参数、单值（一颗星）可变参数、键值对（两颗星）可变参数，使用时必须按照前述顺序书写。
def do_something(name, age, gender='男', *args, **kwds):
    print('姓名：%s，年龄：%d，性别：%s' % (name, age, gender))
    print(args)
    print(kwds)


print(do_something('dudu', 50, '男', 175, 75, math=99, english=90))
