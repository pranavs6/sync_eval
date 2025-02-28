for _ in range(int(input())):
    n, x, k = map(int, input().split())
    s = input().strip()
    p = [0] * (n + 1)
    
    for i in range(n):
        p[i + 1] = p[i] + (1 if s[i] == 'R' else -1)
    
    f = None
    for i in range(1, n + 1):
        if x + p[i] == 0:
            f = i
            break
    
    if f is None or f > k:
        print(0)
        continue
    
    c, r, cyc = 1, k - f, None
    for i in range(1, n + 1):
        if p[i] == 0:
            cyc = i
            break
    
    if cyc:
        c += r // cyc
        r %= cyc
        for i in range(1, r + 1):
            if p[i] == 0:
                c += 1
                break
    
    print(c)

