def soln(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for i in intervals:
        if len(merged) == 0:
            merged.append(i)
        else:
            m = merged[-1]
            if i[0] > m[1]:
                merged.append(i)
            else:
                m[1] = max(i[1], m[1])
    return merged


print(soln([[1, 3], [2, 6], [8, 10], [15, 18]]))
