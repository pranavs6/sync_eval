for _ in range(int(input())):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    half_avg = (sum(arr) / n) / 2
    rc, pc = 0, 0
   
    if n <= 2:
        print(-1)
        continue

    for person in arr:
        if person < half_avg: 
            pc += 1
        else:
            rc += 1
    
    if rc < pc: 
        print(0)
    else:
        val = (arr[pc + 1] - half_avg) * (n * 2) + 1
        print(int(val))

