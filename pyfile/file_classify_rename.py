import datetime
import os
import re
import shutil

import exifread
from tqdm import tqdm


def classify_pic_by_exif():
    src_dir = os.path.abspath(r"/Users/xhzh/yxFiles/_pic/移动硬盘备份/picTest")
    dst_dir = os.path.abspath(r"/Users/xhzh/yxFiles/_pic/移动硬盘备份/datePic")
    # 建立目标目录
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    file_num = 0
    pic_num = 0
    classify_num = 0
    if os.path.exists(src_dir):
        for root, dirs, files in os.walk(src_dir):
            for file in tqdm(files):
                file_num = file_num + 1
                if re.search(r'\.jpg$', file) is not None:
                    pic_num = pic_num + 1

                    str_time = ""
                    src_file = os.path.join(root, file)
                    exif = exifread.process_file(open(src_file, 'rb'))
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

                    if time is not None or originalTime is not None:
                        classify_num = classify_num + 1
                        # 只处理能获取到拍摄时间的文件
                        date_path = str_time[0:10].replace(":", "")
                        date_dir = os.path.join(dst_dir, date_path[0:4] + "-" + date_path[4:6])
                        # 按日期建立目录
                        if not os.path.exists(date_dir):
                            os.makedirs(date_dir)
                        # 剪切到相关日期目录
                        # shutil.move(src_file, date_dir)
                        newFile = date_path + "-" + classify_num.__str__() + ".jpg"
                        new_file = os.path.join(date_dir, newFile)
                        shutil.move(src_file, new_file)

                        print("--->" + file + "--->" + newFile)
                    else:
                        str_time = ""

                        print("--->获取不到图片exif信息")
                else:
                    print("--->该文件不是jpg图片")

    print("文件个数", file_num, "图片个数", pic_num, "分类图片数", classify_num)


def classify_pic_by_ctime():
    src_dir = os.path.abspath(r"/Users/xhzh/yxFiles/_pic/移动硬盘备份/picTest")
    dst_dir = os.path.abspath(r"/Users/xhzh/yxFiles/_pic/移动硬盘备份/phonePic")
    # 建立目标目录
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    file_num = 0
    pic_num = 0
    if os.path.exists(src_dir):
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                file_num = file_num + 1
                if re.search(r'\.jpg$', file) is not None:
                    pic_num = pic_num + 1

                    src_file = os.path.join(root, file)

                    # 只处理能获取到拍摄时间的文件
                    date_path = get_date(os.stat(src_file).st_ctime)
                    date_dir = os.path.join(dst_dir, date_path[0:4] + "-" + date_path[4:6])
                    # 按日期建立目录
                    if not os.path.exists(date_dir):
                        os.makedirs(date_dir)
                    # 剪切到相关日期目录
                    # shutil.move(src_file, date_dir)
                    newFile = date_path + "-" + pic_num.__str__() + ".jpg"
                    new_file = os.path.join(date_dir, newFile)
                    shutil.move(src_file, new_file)

                    print("--->" + file + "--->" + newFile)

            else:
                print("--->该文件不是jpg图片")

    print("文件个数", file_num, "图片个数", pic_num)


def get_date(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y%m%d')


if __name__ == "__main__":
    classify_pic_by_ctime()
