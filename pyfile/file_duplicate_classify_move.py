import datetime
import hashlib
import os
import re
import shutil

import exifread
from PIL import Image


def get_file_hash(src_file):
    with open(src_file, 'rb') as f:
        line = f.readline()
        md5_hash = hashlib.md5()
        while line:
            md5_hash.update(line)
            line = f.readline()
        return md5_hash.hexdigest()


def get_date(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y%m%d')


def get_pic_hash(src_file, hasExif):
    file_info = os.stat(src_file)

    # 获取文件hash
    try:
        file_hash = get_file_hash(src_file)
    except:
        file_hash = 'file_hash'

    # 获取长宽
    try:
        img = Image.open(src_file)
        img_size = img.size.__str__()
    except:
        img_size = '(img_size)'

    if hasExif:
        # 获取exif信息-尤其是拍摄时间
        try:
            exif = exifread.process_file(open(src_file, 'rb'))
        except:
            exif = {}
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

        return file_hash + "/" + file_info.st_size.__str__() + "/" + img_size + "/" + originalTime.__str__() + "/" + time.__str__() + "/" + xsolution.__str__() + "*" + ysolution.__str__()
    else:
        return file_hash + "/" + file_info.st_size.__str__() + "/" + img_size + "/" + get_date(file_info.st_ctime)


def strip_duplicate_pic(src_dir):
    phone_dir = os.path.abspath(r"/Users/xhzh/yxFiles/_pic/_时间备份/phoneDel")

    # 建立目标目录
    if not os.path.exists(phone_dir):
        os.makedirs(phone_dir)

    file_set = set()
    file_num = 0
    del_num = 0
    if os.path.exists(src_dir):
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
        for root, dirs, files in os.walk(src_dir):
            for file in files:

                if re.search(r'\.jpg$', file) is not None:
                    src_file = os.path.join(root, file)
                    try:
                        exif = exifread.process_file(open(src_file, 'rb'))
                    except:
                        exif = {}
                    if "Image DateTime" in exif:
                        time = exif['Image DateTime']
                    else:
                        time = None
                    if "EXIF DateTimeOriginal" in exif:
                        originalTime = exif['EXIF DateTimeOriginal']
                    else:
                        originalTime = None

                    file_num = file_num + 1
                    hasExif = time is not None or originalTime is not None
                    file_hash = get_pic_hash(src_file, hasExif)

                    if file_hash in file_set:
                        del_num = del_num + 1
                        if hasExif:
                            # 删除hasExif图片
                            os.remove(src_file)
                        else:
                            shutil.move(src_file, phone_dir)

                    file_set.add(file_hash)
                    print(file + "--->" + file_hash)

    print("图片个数", file_num, "去重图片", del_num)


def classify_pic_by_time(src_dir):
    month_dir = os.path.abspath(r"/Users/xhzh/yxFiles/_pic/_时间备份/monthPic")
    phone_dir = os.path.abspath(r"/Users/xhzh/yxFiles/_pic/_时间备份/phonePic")

    # 建立目标目录
    if not os.path.exists(month_dir):
        os.makedirs(month_dir)
    # 建立目标目录
    if not os.path.exists(phone_dir):
        os.makedirs(phone_dir)

    file_num = 0
    pic_num = 0
    pic_exif_num = 0
    pic_phone_num = 0
    if os.path.exists(src_dir):
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                file_num = file_num + 1
                if re.search(r'\.jpg$', file) is not None:
                    pic_num = pic_num + 1

                    str_time = ""
                    src_file = os.path.join(root, file)
                    try:
                        exif = exifread.process_file(open(src_file, 'rb'))
                    except:
                        exif = {}
                    if "Image DateTime" in exif:
                        time = exif['Image DateTime']
                        str_time = time.__str__()
                    else:
                        time = None
                    if "EXIF DateTimeOriginal" in exif:
                        originalTime = exif['EXIF DateTimeOriginal']
                        str_time = originalTime.__str__()
                    else:
                        originalTime = None

                    hasExif = time is not None or originalTime is not None

                    if hasExif:
                        pic_exif_num = pic_exif_num + 1
                        # 只处理能获取到拍摄时间的文件
                        date_path = str_time[0:10].replace(":", "")
                        date_dir = os.path.join(month_dir, date_path[0:4] + "-" + date_path[4:6])
                        # 按日期建立目录
                        if not os.path.exists(date_dir):
                            os.makedirs(date_dir)
                        # 剪切到相关日期目录
                        # shutil.move(src_file, date_dir)
                        newFile = date_path + "-" + pic_exif_num.__str__() + ".jpg"
                        new_file = os.path.join(date_dir, newFile)
                        shutil.move(src_file, new_file)

                        print(file + "--->" + newFile)
                    else:
                        pic_phone_num = pic_phone_num + 1

                        src_file = os.path.join(root, file)

                        # 只处理能获取到拍摄时间的文件
                        date_path = get_date(os.stat(src_file).st_ctime)
                        date_dir = os.path.join(phone_dir, date_path[0:4] + "-" + date_path[4:6])
                        # 按日期建立目录
                        if not os.path.exists(date_dir):
                            os.makedirs(date_dir)
                        # 剪切到相关日期目录
                        # shutil.move(src_file, date_dir)
                        newFile = date_path + "-" + pic_phone_num.__str__() + ".jpg"
                        new_file = os.path.join(date_dir, newFile)
                        shutil.move(src_file, new_file)

                        print(file + "--->" + newFile)

                else:
                    print(file + "--->不是jpg图片")

    print("文件个数", file_num, "图片个数", pic_num, "EXIF图片个数", pic_exif_num, "手机图片数", pic_phone_num)


if __name__ == "__main__":
    srcDir = os.path.abspath(r"/Users/xhzh/yxFiles/_pic/_分类备份")
    strip_duplicate_pic(srcDir)
    classify_pic_by_time(srcDir)
