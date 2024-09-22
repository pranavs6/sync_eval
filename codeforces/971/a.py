for _ in range(int(input())):
    a, b = map(int, input().split())
    res = max(a, b)
    for c in range(a , b + 1):
        res = min(((c-a) + (b-c)), res)
    print(res)
