for _ in range(int(input())):
    nums, thr = map(int,input().split())
    arr = list(map(int, input().split()))
    cnt, rg = 0, 0

    for i in range(nums):
        if arr[i] == 0 and rg>0:
            cnt += 1
            rg -= 1
        elif arr[i] >= thr:
            rg += arr[i]

    print(cnt)
