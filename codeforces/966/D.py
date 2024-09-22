for _ in range(int(input())):
    elem_c = int(input())
    num_arr = list(map(int, input().split()))
    lr_arr = input()
    res, l, r = 0, 0, len(lr_arr)-1
    
    while l <= r:
        while l <= r and lr_arr[l] != 'L': l += 1
        while l <= r and lr_arr[r] != 'R': r -= 1
        if l < r:
            res += sum(num_arr[l:r+1])
            l += 1
            r -= 1
        elif l == r:
            res += num_arr[l]
            break
    
    print(res)

