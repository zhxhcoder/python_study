import datetime
import os
import re
import shutil

import exifread
from tqdm import tqdm


# get_pic_hash
def get_pic_hash(file):
    file_info = os.stat(file)
    exif = exifread.process_file(open(file, 'rb'))

    if "Image DateTime" in exif:
        time = exif['Image DateTime']
    else:
        time = "time"

    if "EXIF DateTimeOriginal" in exif:
        originalTime = exif['EXIF DateTimeOriginal']
    else:
        originalTime = "shotTime"

    if "Image XResolution" in exif:
        xsolution = exif['Image XResolution']
    else:
        xsolution = "xx"

    if "Image ImageWidth" in exif:
        width = exif['Image ImageWidth']
    else:
        width = "ww"

    if "Image ImageLength" in exif:
        length = exif['Image ImageLength']
    else:
        length = "ll"

    return file_info.st_size.__str__() + "/" + originalTime.__str__() + "/" + time.__str__() + "/" + xsolution.__str__() + "/" + length.__str__() + "*" + width.__str__()


def get_time_second(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d/%H:%M:%S')


def strip_duplicate_pic():
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
            for file in tqdm(files):

                if re.search(r'\.jpg$', file) is not None:
                    src_file = os.path.join(root, file)

                    exif = exifread.process_file(open(src_file, 'rb'))
                    if "Image DateTime" in exif:
                        time = exif['Image DateTime']
                    else:
                        time = None
                    if "EXIF DateTimeOriginal" in exif:
                        originalTime = exif['EXIF DateTimeOriginal']
                    else:
                        originalTime = None

                    if time is not None or originalTime is not None:
                        file_num = file_num + 1
                        file_hash = get_pic_hash(src_file)

                        if file_hash in file_set:
                            del_num = del_num + 1
                            shutil.move(src_file, dst_dir)
                            # os.remove(src_file)

                        file_set.add(file_hash)

                        print("--->" + file
                              + "--->" + file_hash)

    print("图片个数", file_num, "去重图片", del_num)


if __name__ == "__main__":
    strip_duplicate_pic()
