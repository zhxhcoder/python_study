def readFile(s):
    f = open(s)
    if f is not None:
        line = f.readline()
        while line:
            print(line)
            line = f.readline()
        f.close()


if __name__ == "__main__":
    readFile("/Users/xhzh/Desktop/etfbak8")
