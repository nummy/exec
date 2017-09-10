n = int(input())
points = []
for _ in range(n):
    x, y = map(float, input().split())
    points.append([x,y,0])


def merge(left, right):
    merged = []
    i = 0 
    j = 0
    while i < len(left) and j < len(right):
        if isSmall(left[i], right[j]):
            for item in right[j:]:
                if(left[i][0] < item[0] and left[i][1] < item[1]):
                    item[2] += 1
            merged.append([left[i][0], left[i][1], left[i][2]])
            i += 1
        else:
            for item in left[i:]:
                if(item[0] > right[j][0] and item[1] > right[j][1]):
                    item[2] += 1
            merged.append([right[j][0], right[j][1], right[j][2]])
            j += 1
    for item in left[i:]:
        merged.append([item[0], item[1], item[2]])
    for item in right[j:]:
        merged.append([item[0], item[1], item[2]])
    return merged 



def isSmall(point1, point2):
    if point1[0] < point2[0]:
        return True
    elif point1[0] == point2[0]: 
        if point1[1] < point2[1]:
            return True
    return False


 
def merge_sort(points):
    if len(points) <= 1:
        return points
    num = len(points) // 2
    left = merge_sort(points[:num])
    right = merge_sort(points[num:])
    res = merge(left, right)
    return res


for item in merge_sort(points):
    print(item[2])