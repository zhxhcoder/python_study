ret0 = lambda x: x ** 2
print(ret0(3))

ret1 = map(lambda x: x ** 2, range(10))
print(list(ret1))

ret2 = filter(lambda x: x % 2 == 0, range(1, 10))
print(list(ret2))
