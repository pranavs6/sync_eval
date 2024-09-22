for _ in range(int(input())):
    n = int(input())
    if n == 0 :
        print(1)
        break
    elif n % 2 == 0 :
        print(-1)
        break
    else:
        res = [i for i in range(1, n+1)]
        for i in range(1, n, 2):
            res[i], res[i + 1] = res[i + 1], res[i]
        print(" ".join(map(str, res)))
