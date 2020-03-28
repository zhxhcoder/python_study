def html_tags(tag_name):
    def wrapper_(func):
        def wrapper(*args, **kwargs):
            content = func(*args, **kwargs)
            return "<{tag}>{content}</{tag}>".format(tag=tag_name, content=content)

        return wrapper

    return wrapper_


@html_tags("b")
def hello(name='zhxh'):
    return 'hello {}!'.format(name)


# 不用@的写法如下
# hello = html_tag('b')(hello)
# html_tag('b')是一个闭包，它接受一个函数，并返回一个函数

print(hello())  # <b>hello zhxh!</b>
print(hello('world'))  # <b>hello world!</b>
