import math
results = []
for _ in range(int(input())):
    x, y, k = map(int, input().split())
    cx, cy = math.ceil(x / k), math.ceil(y / k)
    print(cx, cy)
    if cx > cy:
        results.append((2 * cx) - 1)
    elif cy > cx:
        results.append(cy * 2)
    elif cx == cy:
        results.append(cx * 2)
for r in results:
    print(r)

