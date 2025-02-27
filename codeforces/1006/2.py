for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    a = s.count('-')
    b = s.count('_')
    if a < 2:
        print(0)
    else:
        print(b * (a // 2) * ((a + 1) // 2))

