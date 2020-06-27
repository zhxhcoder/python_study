import os
import re
import shutil

from tqdm import tqdm


def copy_file(path, Target_area):  # 传入需要遍历的根目录和需要复制到的区域
    global Suffix_name
    path_list = os.listdir(path)
    for new_path in path_list:
        new_path = os.path.join(path, new_path)
        if os.path.isdir(new_path):
            copy_file(new_path, Target_area)
            print("目录")
        elif os.path.isfile(new_path):
            Suffix_name = os.path.splitext(new_path)[1]
        if Suffix_name in [".bmp", ".gif", ".png", ".jpg"]:  # 指定文件后缀名，从而指定文件格式
            shutil.copy(new_path, Target_area)
            print("文件")
        else:
            print("there is sth wrong")

        copy_file(path, Target_area)


def searchFile():
    # 规范化绝对路径
    src_dir = os.path.abspath(r"/Users/xhzh/yxFiles/_pic/cpyTest")

    path_list = os.listdir(src_dir)
    for new_path in path_list:
        new_path = os.path.join(src_dir, new_path)
        if os.path.isdir(new_path):
            copyRenameFile(new_path)
            print("-源文件目录->" + new_path)


def copyRenameFile(newSrcDir):
    src_dir = os.path.abspath(newSrcDir)
    dst_dir = os.path.abspath(r"/Users/xhzh/yxFiles/_pic/leetcodeGif")

    # 建立目标目录
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    if os.path.exists(src_dir):
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
        for root, dirs, files in os.walk(src_dir):
            for file in tqdm(files):

                if re.search(r'\.gif$', file) is not None:
                    src_file = os.path.join(root, file)
                    shutil.copy(src_file, dst_dir)
                    print("-->" + src_file)


if __name__ == "__main__":
    searchFile()
