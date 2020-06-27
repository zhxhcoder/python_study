import datetime
import os

from tqdm import tqdm


# 如果大小一样且，创建时间是在同一分钟
def is_same_file(file_info1, file_info2):
    if file_info1.st_size == file_info2.st_size and get_time_second(file_info1.st_ctime) == get_time_second(
            file_info2.st_ctime):
        return True
    return False


def get_time_second(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


def strip_duplicate_file():
    src_dir = os.path.abspath(r"/Users/xhzh/yxFiles/_pic/picTest")

    index = 0
    if os.path.exists(src_dir):
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
        for root, dirs, files in os.walk(src_dir):
            for i, file in enumerate(tqdm(files)):
                index = index + 1
                src_file = os.path.join(root, file)
                fileInfo = os.stat(src_file)
                print(index.__str__() + "--->" + file
                      + " 大小：" + fileInfo.st_size.__str__()
                      + " 创建时间：" + get_time_second(fileInfo.st_ctime).__str__())


if __name__ == "__main__":
    strip_duplicate_file()
