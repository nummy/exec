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
    rcounter = 0
    lcounter = 0
    while i < len(left) and j < len(right):
        if isSmall(left[i], right[j]):
            if(left[i][0] < right[j][0] and left[i][1] < right[j][1]):
                rcounter += 1
            merged.append(left[i][2]+lcounter)
            i += 1
        else:
            if(left[i][0] > right[j][0] and left[i][1] > right[j][1]):
                lcounter += 1
            merged.append(right[j][2] + rcounter)
            j += 1
    for item in left[i:]:
        merged.append(item[2]+lcounter)
    for item in right[j:]:
        merged.append(item[2]+rcounter)
    return merged 

def isSmall(point1, point2):
    if point1[1] < point2[1]:
        return True
    elif point1[1] == point2[1]: 
        if point1[0] < point2[0]:
            return True
    return False

for item in merge(left, right):
    print(item)