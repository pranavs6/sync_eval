from collections import Counter

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ctr = Counter(arr)
    max_occ = max(ctr.values())
    print(n-max_occ)
