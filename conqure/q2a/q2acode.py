# 读取文件 把左边3个因素 和右边3个因素
# 左边和右边均生成一个二维list 作为返回
number = 10
stropen = ('./input/n{}_0.in').format(number)
strout = ('./output/n{}_0.out').format(number)

def openfile():
    global stropen
    leftlist  = []
    rightlist = []
    flag = True
    with open(stropen, 'r') as f:
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
            sublist[2] = int(sublist[2])
            if flag:
                leftlist.append(sublist)
            else:
                rightlist.append(sublist)
    return leftlist, rightlist


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
            if(j>=int(number/2)):
                j = int(number/2 - 1)
            merged.append(right[j])
            j += 1

        else:
            merged.append(left[i])
            counter += 1
            i += 1
            if(i>=int(number/2)):
                i = int(number/2 -1)
    # print(merged)
    return merged


# def merga(left, right):
#     global number
#     leftindex = []
#     leftnumdict = {}
# # 将left内容按照important从小到大排列
#     i = 0
#     for point in left:
#         leftnumdict[str(i)] = point[2]
#         i = i + 1
#     print(leftnumdict)
#     leftnumlist = sorted(leftnumdict.items(), key=lambda d:d[1])
#
#     for numlist in leftnumlist:
#         leftindex.append(int(numlist[0]))
#     print(leftindex)
#
#     rightindex = []
#     rightnumdict = {}
# # 将right内容按照important从小到大排列
#     i = 0
#     for point in right:
#         rightnumdict[str(i)] = point[2]
#         i = i + 1
#     print(rightnumdict)
#     rightnumlist = sorted(rightnumdict.items(), key=lambda d:d[1])
#
#     for numlist in rightnumlist:
#         rightindex.append(int(numlist[0]))
#     print(rightindex)
#
#     mergedlist = []
#     i = j = 0
#     while i< int(number/2) and j< int(number/2):
#         if left[leftindex[i]][0] > right[rightindex[j]][0] and \
#             left[leftindex[i]][0] > right[rightindex[j]][0]:
#             left[leftindex[i]][2] = left[leftindex[i]][2] + 1
#             mergedlist.append(left[leftindex[i]])
#             i = i + 1
#
#         else:
#             right[rightindex[j]][2] = right[rightindex[j]][2]+1
#             mergedlist.append(right[rightindex[j]])
#             j = j + 1
#             # if j>=5:
#             #     while i< int(number/2):
#             #         mergedlist.append(left[leftindex[i]])
#     print(mergedlist)
#     print(i)
#     print(j)

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
    merged = merga(leftlist, rightlist)
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

