n = int(input())
left, right = [], []
l = int(input())
for _ in range(l):
    x, y, imp = map(float, input().split())
    left.append([x, y, imp])
r = int(input())
for _ in range(r):
    x, y, imp = map(float, input().split())
    right.append([x, y,imp])

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
    if point1[0] == point2[0]: 
        if point1[0] < point2[0]:
            return True
    return False

lst = merge(left, right)
lst = sorted(lst, key=lambda item:(item[0], item[1]))
for item in lst:
    print(int(item[2]))