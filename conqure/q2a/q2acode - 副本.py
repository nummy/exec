# 读取文件 把左边3个因素 和右边3个因素
# 左边和右边均生成一个二维list 作为返回
def openfile():
    number = 10
    leftlist  = []
    rightlist = []
    flag = True
    str = ('./input/n{}_0.in').format(number)
    print(str)
    with open(str, 'r') as f:
        for line in f.readlines():
            sublist = []
            a = line.replace('\n', '')
            b = a.split(' ')
            sublist = [float(i) for i in b]
            # print(sublist)
            length = len(sublist)
            if length == 1:
                flag = not flag
                continue
            if flag:
                leftlist.append(sublist)
            else:
                rightlist.append(sublist)
    return leftlist, rightlist


def merga(left, right)

# 给出了2维点(x,y)因为要每一个点的2个维度都要比其他的点大
# 所以可以把这个点的2个维度做一下乘积，比较这个乘积的大小就可以了
if __name__ == '__main__':
    leftlist, rightlist = openfile()
    merga(leftlist, rightlist)
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

