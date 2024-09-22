t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    valid = True
    for i in range(1, n):
        if abs(a[i] - a[i - 1]) > 1:
            valid = False
            break
    
    if valid:
        print("YES")
    else:
        print("NO")

