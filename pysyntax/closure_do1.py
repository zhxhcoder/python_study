# 函数返回值为函数，Python 函数为第一类对象，可以赋值给变量，可以作为参数传递，可以从函数中返回。
def outer_func():
    loc_list = []

    def inner_func(name):
        loc_list.append(len(loc_list) + 1)
        print('%s loc_list = %s' % (name, loc_list))

    return inner_func


def func_dec(func):
    def wrapper(*args):
        if len(args) == 2:
            func(*args)
        else:
            print('Error! Arguments = %s' % list(args))

    return wrapper


@func_dec
def add_sum(*args):
    print(sum(args))


# add_sum = func_dec(add_sum)
args = range(1, 3)
add_sum(*args)

if __name__ == "__main__":
    clo_func_0 = outer_func()
    clo_func_0('clo_func_0')
    clo_func_0('clo_func_0')
    clo_func_0('clo_func_0')
    clo_func_1 = outer_func()
    clo_func_1('clo_func_1')
    clo_func_0('clo_func_0')
    clo_func_1('clo_func_1')
