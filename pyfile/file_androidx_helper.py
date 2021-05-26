# -*- coding: utf-8 -*-
# androidx 整体替换


def traverse_file_replace(src_dir, replace_csv):
    # 遍历文件，并替换文件中的 特殊字符
    import datetime
    start = datetime.datetime.now()

    # 读取csv文件
    dic = {}
    import csv
    with open(replace_csv) as f:
        row = csv.reader(f, delimiter=',')
        for r in row:
            dic[r[0]] = r[1]

    allowFileNum = 0

    import os
    if os.path.exists(src_dir):
        for root, dirs, files in os.walk(src_dir):
            for file in files:
                src_file = os.path.join(root, file)

                ALLOWED_EXTENSIONS = {'java', 'kt', 'xml', 'gradle'}
                allowed_file = '.' in src_file and src_file.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
                if allowed_file:
                    allowFileNum = allowFileNum + 1
                    # 替换csv文件中的key，value
                    try:
                        replace_file(src_file, dic)
                    except:
                        print('异常文件:------> %s' % src_file)
                        continue

    end = datetime.datetime.now()
    print('检索文件: %s 个' % allowFileNum)
    print('耗时: %s 秒' % (end - start))


def replace_file(src_file, dic):
    print(src_file)
    # 循环csv文件
    fp = open(src_file, 'r')
    lines = fp.readlines()  # 打开文件，读入每一行
    fp.close()

    fp = open(src_file, 'w+')
    for s in lines:
        # 需要替换文件中的多个字段，并写入新文件fp中
        for key, value, in dic.items():
            s = s.replace(key, value)

        fp.write(s)

    fp.close()  # 关闭文件


if __name__ == '__main__':
    try:
        print("action start...")
        traverse_file_replace("/Users/xhzh/yxFiles/gitProj/CreditWealthProj",
                              "androidx-class-mapping.csv")

    except Exception as e:
        print(e)
        input("Please Enter To Finish...")
