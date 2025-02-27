t = int(input())
for _ in range(t):
    n = int(input())
    q, r = divmod(n, 15)
    print(q * 3 + min(3, r + 1))

