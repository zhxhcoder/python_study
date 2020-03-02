import os
import shutil

print(os.getcwd())  # /usr/local/bin/python3.8 /Users/xhzh/yxFiles/pythonProj/python_study/file/file_do.py


def edit_something(file):
    file.write("第一行\n")
    file.write("第二行\n")
    print('写入\n', file.readable())


f = open("/Users/xhzh/hello.py", "w+")
print(f.name)
shutil.copy('/Users/xhzh/hello.py', '/Users/xhzh/Desktop/first.py')


def add_something(file):
    file.write("第三行\n")
    file.write("第四行\n")
    print('添加\n', file.readable())


with open('/Users/xhzh/hello.py', 'w') as f:
    edit_something(f)

with open('/Users/xhzh/hello.py', 'a') as f:
    add_something(f)

print("################建立文件####################")

for i in range(1, 11):
    oldFileName = "/Users/xhzh/test/hello" + str(i) + ".py"
    f = open(oldFileName, "w")
    f.write(oldFileName)
    print(oldFileName)

print("################建立子件夹####################")

innerDir = "/Users/xhzh/test/inner/"
if os.path.exists(innerDir):
    shutil.rmtree(innerDir)  # 空目录、有内容的目录都可以删

os.mkdir(innerDir)

for i in range(1, 11):
    oldFileName = innerDir + "hi" + str(i) + ".py"
    f = open(oldFileName, "w")
    f.write(oldFileName)
    print(oldFileName)

    newFileName = oldFileName.replace('hi', 're')
    os.rename(oldFileName,newFileName)
    print(newFileName)


print("################遍历文件####################")
