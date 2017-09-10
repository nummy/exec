def merge(left, right):
    merged = []
    left, left_imp = zip(*left)
    right, right_imp = zip(*right)
    i = j = counter = 0
    Y_COORD = 1
    while len(merged) != len(left) + len(right):
        if right[j][Y_COORD] <= left[i][Y_COORD]:
            merged.append((right[j], right_imp[j] + counter))
            j += 1
        else:
            merged.append((left[i], left_imp[i]))
            counter += 1
            i += 1
    return merged
