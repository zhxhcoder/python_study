import datetime
import os
import shutil



# 如果大小一样且，创建时间是在同一分钟
def is_same_file(file1, file2):
    file_info1 = os.stat(file1)
    file_info2 = os.stat(file2)
    if file_info1.st_size == file_info2.st_size and get_time_second(file_info1.st_ctime) == get_time_second(
            file_info2.st_ctime):
        return True
    return False


# get_file_hash获得文件的主键
def get_file_hash(file):
    file_info = os.stat(file)
    return file_info.st_size.__str__() + "/" + get_time_second(file_info.st_ctime)


def get_time_second(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d/%H:%M:%S')


def strip_duplicate_file():
    src_dir = os.path.abspath(r"/Users/xhzh/yxFiles/_pic/移动硬盘备份/picTest")

    dst_dir = os.path.abspath(r"/Users/xhzh/yxFiles/_pic/移动硬盘备份/duplicate")
    # 建立目标目录
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    file_set = set()
    file_num = 0
    del_num = 0
    if os.path.exists(src_dir):
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                file_num = file_num + 1
                src_file = os.path.join(root, file)
                file_hash = get_file_hash(src_file)

                if file_hash in file_set:
                    del_num = del_num + 1
                    shutil.move(src_file, dst_dir)
                    # os.remove(src_file)

                file_set.add(file_hash)

                print("--->" + file
                      + "--->" + file_hash)

    print("文件个数", file_num, "去重文件", del_num)


if __name__ == "__main__":
    strip_duplicate_file()
