def readFile(s):
    f = open(s)
    if f is not None:
        line = f.readline()
        while line:
            print(line)
            getFieldNum(line)
            line = f.readline()
        f.close()


def readFiles(s):
    f = open(s)
    if f is not None:
        lines = f.readlines()
        print(lines)
        f.close()


def getFieldNum(line):
    import re
    matches = re.findall(r'\S+', line)
    if matches.__len__() == 17:
        print(matches[1] + "输入成功")
    else:
        print(matches)


if __name__ == "__main__":
    readFile("/Users/xhzh/Desktop/fund.txt")
