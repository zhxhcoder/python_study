import os

os.getcwd()

print(os.getcwd())

f = open("/Users/xhzh/test.txt")  # 在本文件夹下面的一个文件


def do_something():
    pass


with open('/Users/xhzh/test.txt', 'r') as f:
    do_something()
