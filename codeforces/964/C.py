for _ in range(int(input())):
    t, s, tot = map(int, input().split())
    arr = []
    for i in range(0, t):
        arr.append(list(map(int, input().split())))
    arr = arr + [[0,0], [tot,tot]] 
    arr.sort()
    for i in range(1, t + 2):
        if (arr[i][0] - arr[i-1][1]) >= s:
            print("YES")
            break
    else:
        print("NO")
