import os

# 删除大小一样的文件 问题类似于LeetCode26

fileDir = '/Users/xhzh/fileDo/jpg1'


# 遍历文件夹
def walk_file(file):
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
            file_name = os.path.join(root, f)
            print(file_name, os.stat(file_name).st_size)

        # 遍历所有的文件夹
        for d in dirs:
            print(os.path.join(root, d))


walk_file(fileDir)
