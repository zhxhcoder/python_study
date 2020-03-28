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
