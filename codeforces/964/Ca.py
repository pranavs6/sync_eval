for _ in range(int(input())):
    ts, sm, tot = map(int, input().split())
    res = "NO"
    arr = [i+1 for i in range(tot)]  # initialize the array from 1 to tot
    for i in range(ts):
        x, y = map(int, input().split())
        if x in arr and y in arr:
            arr = arr[:x-1] + [0]*(y-x+1) + arr[y:]
    
    for i in range(len(arr) - sm + 1):
        temp = arr[i:i+sm]
        if all(v == 0 for v in temp):
            res = "YES"
            break
    
    print(res)

