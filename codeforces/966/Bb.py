t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # Sort the seats to check adjacency
    a_sorted = sorted(a)
    
    valid = True
    for i in range(1, n):
        if a_sorted[i] - a_sorted[i - 1] > 1:
            valid = False
            break
    
    if valid:
        print("YES")
    else:
        print("NO")

