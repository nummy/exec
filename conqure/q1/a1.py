n = int(input())
points = []
for _ in range(n):
    p = float(input())
    points.append(p)

nums = list(set(points))
nums.sort()
print(nums)
for i in range(n):
    point = points[i]
    print(nums.index(point))