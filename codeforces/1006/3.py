t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    
    if x & 1 == 0:
        m0 = 1
    else:
        m0 = None
        for k in range(1, 31):
            if ((x >> k) & 1) == 0:
                m0 = 1 << k
                break
        if m0 is None:
            m0 = 1 << 30  

    def R(m):
        return (1 << ((m - 1).bit_length())) - 1 if m > 0 else 0
    
    m = min(n, m0)
    if m == n and R(m) != x:
        while m > 0 and m == n:
            m -= 1
    
    ans = list(range(m))
    if R(m) != x:
        ans.append(x & ~R(m))
    ans += [0] * (n - len(ans))
    
    print(*ans)

