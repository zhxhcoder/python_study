import os
import re
import shutil

from tqdm import tqdm


def searchFile():
    # 规范化绝对路径
    src_dir = os.path.abspath(r"/Users/xhzh/yxFiles/_pic/cpyTest")

    path_list = os.listdir(src_dir)
    for path in path_list:
        new_path = os.path.join(src_dir, path)
        if os.path.isdir(new_path):
            # 源文件目录作为新的gif名
            print("-源文件目录->" + new_path)
            copyRenameFile(path, new_path)


def copyRenameFile(new_file_name, newSrcDir):
    src_dir = os.path.abspath(newSrcDir)
    dst_dir = os.path.abspath(r"/Users/xhzh/yxFiles/_pic/leetcodeGif")

    index = 0
    # 建立目标目录
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    if os.path.exists(src_dir):
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
        for root, dirs, files in os.walk(src_dir):
            for i, file in enumerate(tqdm(files)):
                if re.search(r'\.gif$', file) is not None:
                    if index == 0:
                        newFile = new_file_name + ".gif"
                    else:
                        newFile = new_file_name + index.__str__() + ".gif"

                    src_file = os.path.join(root, file)
                    new_file = os.path.join(dst_dir, newFile)

                    print(new_file)

                    shutil.copy(src_file, new_file)
                    index = index + 1


if __name__ == "__main__":
    searchFile()
