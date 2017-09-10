def planesweep(points):
    n = len(points)
    # If we order by x-asc and tie break with y-desc, we neatly handle duplicate point-vals.
    points = sorted(points, key = lambda xy : (xy[0], -xy[1]))
    importance = [0]*n
    bst = SortedList()
    for ix,(x,y) in enumerate(points):
        importance[ix] = bst.bisect_left(y)
        bst.add(y)
    return list(zip(points,importance))