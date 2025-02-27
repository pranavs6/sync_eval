for _ in range(int(input())):
    arr, target, nos = map(int, input().split())
    target = abs(target)
    m = target//nos
    if target % nos != 0:
        m += 1
    if m <= arr:
        print(m)
    else:
        print(-1)
