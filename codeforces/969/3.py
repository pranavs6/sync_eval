import math

results = []

for _ in range(int(input())):
    n, a, b = map(int,input().split())
    c = list(map(int, input().split()))
    
    min_c = min(c)
    max_c = max(c)
    
    range_c = max_c - min_c
    
    if a == b:
        results.append(range_c)
    else:
        results.append(min(range_c, math.gcd(a, b)))

print("\n".join(map(str, results)))

