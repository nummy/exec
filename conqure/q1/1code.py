# 打开文件
# 得到3个返回，分别是文件内容列表，文件下标、内容字典
def openfile():
    valdict = {}
    posdict = {}
    numX  = []
    with open('./input/n1000_0.in', 'r') as f:
        i = 1
        for line in f.readlines():
            line = (line.replace('\n', ''))
            valdict[line] = i
            posdict[str(i)] = int(line)
            numX.append(int(line))
            i = i + 1
    return numX


# 写入文件
def write_file(outval):
    with open('./output/n1000_0.out', 'w') as f:
        for line in outval:
            new_line = str(line) + '\n'
            f.writelines(new_line)


# 主要使用了sort进行排序
# https://www.zhihu.com/question/36280272
# 效率最差是nlogn

if __name__ == '__main__':
    numX = openfile()
    length = len((numX))
    # 将文件内容list弄成不重复的并对其进行排序
    snumX = sorted(set(numX))
    snumY = sorted(numX)
    print(snumX)
    outlist = []
    for i in range(length):
        # 通过文件下表、内容字典 下表找到该行对应的文件内容
        # 然后通过排序后的文件内容知道这个value在其他多少个
        # values前面
        outlist.append(snumX.index(snumY[i]))
    write_file(outlist)

