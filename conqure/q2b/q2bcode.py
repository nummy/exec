# 读取文件 把左边3个因素 和右边3个因素
# 左边和右边均生成一个二维list 作为返回
number = 10
stropen = ('./input/n{}_0.in').format(number)
strout = ('./output/n{}_0.out').format(number)


def openfile():
    i = 0
    global stropen
    leftlist  = []
    rightlist = []
    with open(stropen, 'r') as f:
        for line in f.readlines():
            sublist = []
            a = line.replace('\n', '')
            b = a.split(' ')
            sublist = [float(i) for i in b]

            length = len(sublist)
            if length == 1:
               continue
            i = i+1
            if i <= number/2:
                leftlist.append(sublist)
            else:
                rightlist.append(sublist)

    return leftlist, rightlist


# 将整体文件分成两份，分别作为左边list和右边list
# 计算两个点的乘积 这里使用的方法和
def listsqare(left, right):
    leftposdict = {}
    leftvallist = []
    rightposdict = {}
    rightvallist = []

    i = 1
    for point in left:
        # 记录一下这个点所在的行数

        a = point[0] * point[1]
        if point[0]<0 and point[1]<0:
            a = 0 - a
        leftposdict[str(i)] = a
        leftvallist.append(a)
        i = i + 1

    i = 1
    for point in right:
        # 记录一下这个点所在的行数
        a = point[0] * point[1]
        if point[0]<0 and point[1]<0:
            a = 0 - a
        # 得到面积
        rightposdict[str(i)] = a
        rightvallist.append(a)
        i = i + 1
    return leftposdict, leftvallist, rightposdict, rightvallist



# 根据example文件代码 修改写出
def merga(left, right):
    global number
    merged = []
    i = j = counter = 0
    Y_COORD = 1
    # print(rightlist)
    while len(merged) != len(left) + len(right):
        if right[j][Y_COORD] <= left[i][Y_COORD]:
            right[j][2] = right[j][2] + counter
            merged.append(right[j])
            j += 1
            if(j>=int(number/2)):
                j = int(number/2 - 1)
        else:
            merged.append(left[i])
            counter += 1
            i += 1
            if(i>=int(number/2)):
                i = int(number/2 -1)
    # print(merged)
    return merged

def write_file(outval):
    global strout
    with open(strout, 'w') as f:
        for line in outval:
            new_line = str(line).replace('[', '')
            new_line = new_line.replace(']', '')
            new_line = new_line + '\n'
            f.writelines(new_line)

# 给出了2维点(x,y)因为要每一个点的2个维度都要比其他的点大
# 所以可以把这个点的2个维度做一下乘积，比较这个乘积的大小就可以了
if __name__ == '__main__':
    leftlist, rightlist = openfile()
    leftposdict, leftvallist, rightposdict, rightvallist = listsqare(leftlist, rightlist)
    leftvallistsortd = sorted(set(leftvallist))
    rightvallistsortd = sorted(set(rightvallist))

    print(leftvallistsortd)
    print(leftposdict)

    i = 1
    for postion in leftlist:
        postion.append(leftvallistsortd.index(leftposdict[str(i)]))
        i = i + 1
    print(leftlist)

    i = 1
    for postion in rightlist:
        postion.append(rightvallistsortd.index(rightposdict[str(i)]))
        i = i + 1
    print(rightlist)
    merged = merga(leftlist, rightlist)
    print(merged)
    # write_file(merged)

    # leftsqare  = []
    # rightsqare = []
    # for left in leftlist:
    #     sublist = []
    #     sublist.append(left[0] * left[1])
    #     sublist.append(left[2])
    #     leftsqare.append(sublist)
    #
    # for right in rightlist:
    #     sublist = []
    #     sublist.append(right[0] * right[1])
    #     sublist.append(right[2])
    #     rightsqare.append(sublist)

