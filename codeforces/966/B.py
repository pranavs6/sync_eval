for _ in range(int(input())):
    pas = int(input())
    arr_a = list(map(int,input().split()))
    arr_p = [0] * pas
    res = []
    main = [0] * (pas+2)
    flag = True
    for itr in range(0, pas):
        arr_p[arr_a[itr]-1] = itr + 1
     
    for i in range(pas):
        if sum(res)==0:
            main[arr_p[i]-1] = i+1
        elif main[arr_p]!=0 or main[arr_p-2]!=0:
            main[arr[p]-1] = i+1
        else: flag = False


    if flag:
        print("YES")
    else:
        print("NO")

