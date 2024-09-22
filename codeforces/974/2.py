for _ in range(int(input())):
    year, line = map(int, input().split())
    ra, rb = year - line + 1, year 
    if (((rb + 1) // 2) - (ra // 2)) % 2 == 0 :
        print("YES")
    else:
        print("NO")
