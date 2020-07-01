import datetime
import hashlib
import os


def get_file_hash(src_file):
    with open(src_file, 'rb') as f:
        line = f.readline()
        md5_hash = hashlib.md5()
        while line:
            md5_hash.update(line)
            line = f.readline()
        return md5_hash.hexdigest()


def get_bytes_hash(src_file, Bytes=1024):
    md5_hash = hashlib.md5()  # 创建一个md5算法对象
    with open(src_file, 'rb') as f:  # 打开一个文件，必须是'rb'模式打开
        while 1:
            data = f.read(Bytes)  # 由于是一个文件，每次只读取固定字节
            if data:  # 当读取内容不为空时对读取内容进行update
                md5_hash.update(data)
            else:  # 当整个文件读完之后停止update
                break
    ret = md5_hash.hexdigest()  # 获取这个文件的MD5值
    return ret


def traverse_file(src_dir):
    start = datetime.datetime.now()
    file_num = 0
    if os.path.exists(src_dir):
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                file_num = file_num + 1
                src_file = os.path.join(root, file)

                print(
                    file + "-->file_hash-->" + get_file_hash(src_file) + "-->bytes_hash-->" + get_bytes_hash(src_file))

    end = datetime.datetime.now()
    print('耗时: %s Seconds' % (end - start))


if __name__ == "__main__":
    srcDir = os.path.abspath(r"/Users/xhzh/yxFiles/_pic/video")
    traverse_file(srcDir)
