# yield 语句仅用以定义生成器函数，而且只能出现在生成器函数内

def infinite():
    n = 1
    while 1:
        yield n
        n += 1


ge = infinite()

print(next(ge))
print(next(ge))
print(next(ge))
print(next(ge))


def test():
    print('step 1')
    x = yield 1


# 二叉树遍历通过
# 生成器可以将非线性化的处理转换成线性化的处理法方式
# 传统的方法是递归来访问和处理，既容易出错也不清晰

def deal_tree(node):
    if not node:
        return
    if node.leftnode:
        for i in deal_tree(node.leftnode):
            yield i
    yield node

    if node.rightnode:
        for i in deal_tree(node.rightnode):
            yield i


def process(node):
    pass


root = None

for node in deal_tree(root):
    process(node)
