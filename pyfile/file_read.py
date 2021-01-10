f = open("/Users/xhzh/Desktop/etfbak8")
if f is not None:
    line = f.readline()
    while line:
        print(line)
        line = f.readline()
    f.close()
