import datetime
import os
import re
import shutil

import exifread
from PIL import Image
from tqdm import tqdm


# get_pic_hash
def get_pic_hash(file, hasExif):
    file_info = os.stat(file)
    # 获取长宽
    img = Image.open(file)

    if hasExif:
        # 获取exif信息-尤其是拍摄时间
        exif = exifread.process_file(open(file, 'rb'))
        if "Image DateTime" in exif:
            time = exif['Image DateTime']
        else:
            time = "dateTime"
        if "EXIF DateTimeOriginal" in exif:
            originalTime = exif['EXIF DateTimeOriginal']
        else:
            originalTime = "originTime"
        if "Image XResolution" in exif:
            xsolution = exif['Image XResolution']
        else:
            xsolution = "xx"
        if "Image YResolution" in exif:
            ysolution = exif['Image YResolution']
        else:
            ysolution = "yy"

        return file_info.st_size.__str__() + "/" + img.size.__str__() + "/" + originalTime.__str__() + "/" + time.__str__() + "/" + xsolution.__str__() + "*" + ysolution.__str__()
    else:
        return file_info.st_size.__str__() + "/" + img.size.__str__() + "/" + get_time_second(file_info.st_ctime)


def get_time_second(timestamp):
    # return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    # 只获取当天
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')


def strip_duplicate_pic():
    # src_dir = os.path.abspath(r"G:\移动硬盘备份\_分类备份\照片\jpg")
    # dst_dir = os.path.abspath(r"G:\移动硬盘备份\_分类备份\照片\duplicate")
    # sole_dir = os.path.abspath(r"G:\移动硬盘备份\_分类备份\照片\sole")

    src_dir = os.path.abspath(r"/Users/xhzh/yxFiles/_pic/移动硬盘备份/picTest")
    dst_dir = os.path.abspath(r"/Users/xhzh/yxFiles/_pic/移动硬盘备份/duplicate")
    sole_dir = os.path.abspath(r"/Users/xhzh/yxFiles/_pic/移动硬盘备份/sole")
    # 建立目标目录
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    # 建立获取不到拍摄时间的图片目录
    if not os.path.exists(sole_dir):
        os.makedirs(sole_dir)

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
                    # 只处理能获取到拍摄时间的文件
                    if time is not None or originalTime is not None:
                        file_num = file_num + 1
                        file_hash = get_pic_hash(src_file, True)

                        if file_hash in file_set:
                            del_num = del_num + 1
                            shutil.move(src_file, dst_dir)
                            # os.remove(src_file)

                        file_set.add(file_hash)
                        print("--->" + file + "--->" + file_hash)
                    else:
                        print("--->" + file + "--->" + get_pic_hash(src_file, False))
                        shutil.move(src_file, sole_dir)

    print("图片个数", file_num, "去重图片", del_num)


if __name__ == "__main__":
    strip_duplicate_pic()
