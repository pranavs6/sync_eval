for _ in range(int(input())):
    n = int(input())
    if n == 1: print(1)
    elif n %2 == 0: print(-1)
    else:
        res = []
        for i in range(1, n+1, 2):
            res.append(i)
        for i in range(2, n+1, 2):
            res.append(i)
        
        print(res)
