for _ in range(int(input())):
    l, r = map(int, input().split())
    o, e = 0, 0
    for i in range(l, r + 1):
        if i % 2 == 0: e += 1
        else: o += 1
    print(o//2, e)
