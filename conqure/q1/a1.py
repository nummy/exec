n = int(input())
points = []
for _ in range(n):
    p = float(input())
    points.append(p)

nums = list(set(points))

def quick_sort(lists, left, right):
    # quick sort
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists

nums = quick_sort(nums, 0, len(nums)-1)

for i in range(n):
    point = points[i]
    print(nums.index(point))