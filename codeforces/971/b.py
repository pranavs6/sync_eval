for _ in range(int(input())):
    arr = []
    n = int(input())
    for i in range(n):
        arr = [str(input()).index("#") + 1] + arr
    for ans in arr:
        print(ans, end = " ")
