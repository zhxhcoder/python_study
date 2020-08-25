# 支持迭代的类

class simple_range(object):
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return self

    def next(self):
        if self.num <= 0:
            raise StopIteration

        temp = self.num
        self.num -= 1
        return temp


a = simple_range(5)
print(a.next())
print(a.next())
print(a.next())
