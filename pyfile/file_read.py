def readFile(s):
    f = open(s)
    if f is not None:
        line = f.readline()
        while line:
            print(line)
            getFieldNum(line)
            line = f.readline()
        f.close()


def getFieldNum(line):
    import re
    matches = re.finditer(r'\S+', line)
    # 打印 a 字符出现的次数
    print(matches)


if __name__ == "__main__":
    readFile("/Users/xhzh/Desktop/etfbak8")
