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
    matches = re.findall(r'\S+', line)
    if matches.__len__() == 17:
        print("成功")
    else:
        print(matches.__len__())


if __name__ == "__main__":
    readFile("/Users/xhzh/Desktop/etfbak8")
