results = []

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(set(list(map(int, input().split()))))
    n = len(arr)
    res = []

    for i in range(m):
        op, l, r = map(str, input().split())
        l, r = int(l), int(r)
        if op == "+":
            for i in range(n):
                if arr[i] in range(max(l, min(arr)), min(max(arr), r) + 1):
                    arr[i] += 1
        else:
            for i in range(n):
                if arr[i] in range(l, r + 1):
                    arr[i] -= 1
        res.append(max(arr))
    results.append(res)

for res in results:
    for i in res:
        print(i, end = " ")
    print()
