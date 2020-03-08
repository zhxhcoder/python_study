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

# 此外，一颗星和两颗星还可用于列表、元组、字典的解包，看起来更像C语言：
c = {'name': 'dudu', 'age': 51}
print(c)
print(*c)
print('name:{name}, age:{age}'.format(**c))

print("######################################三元表达式######################################")
y = 5
print('y是一个负数' if y < 0 else 'y是一个非负数')
print("###################################### with - as######################################")

with open(r"/data/xx.py", 'r') as fp:
    contents = fp.readlines()
    print(contents)

print("######################################列表推导式######################################")
a = [1, 2, 3, 4, 5]
result = list()
for i in a:
    result.append(i * i)

print(result)
print("######################################列表索引的各种######################################")

a = [0, 1, 2, 3, 4, 5]
print(a[2:4])
print(a[-1])

print("######################################lambda函数######################################")
lambda x, y: x + y
(lambda x, y: x + y)(3, 4)  # 因为匿名函数没有名字，使用的时候要用括号把它包起来

a = [1, 2, 3]
for item in map(lambda x: x * x, a):
    print(item, end=',')

print("######################################yield 以及生成器和迭代器######################################")

print("######################################装饰器######################################")

import time


# timer() 是我们定义的装饰器函数，使用@把它附加在任何一个函数（比如do_something）定义之前，就等于把新定义的函数，当成了装饰器函数的输入参数。运行 do_something() 函数，可以理解为执行了timer(do_something) 。细节虽然复杂，不过这么理解不会偏差太大，且更易于把握装饰器的制造和使用。

def timer(func):
    def wrapper(*args, **kwds):
        t0 = time.time()
        func(*args, **kwds)
        t1 = time.time()
        print('耗时%0.3f' % (t1 - t0,))

    return wrapper


@timer
def do_something(delay):
    print('函数do_something开始')
    time.sleep(delay)
    print('函数do_something结束')
