case = 0
res = []

for _ in range(int(input())):
    case += 1
    count, time = map(int, input().split())
    arr = []
    for i in range(count):
        arr.append(int(input()))
    m = min(arr)
    if count >= 2:
        if (2 * count - 3) * m <= time:
            res.append("Case #" + str(case) + ": YES")
        else:
            res.append("Case #" + str(case) + ": NO")
    else:
        if arr[0] <= time:
            res.append("Case #" + str(case) + ": YES")
        else:
            res.append("Case #" + str(case) + ": NO")

for op in res:
    print(op, end = "\n")
