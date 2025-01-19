t = int(input())
res = []

for _ in range(t):
    a, b, d, e = map(int, input().split())
    mfc = 0

    for c in range(-200, 201):  
        fc = 0
        
        if d == b + c:
            fc += 1
        if e == c + d:
            fc += 1
        if c == a + b:
            fc += 1
        
        mfc = max(mfc, fc)
    
    res.append(mfc)

print("\n".join(map(str, res)))

