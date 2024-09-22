import math
for _ in range(int(input())):
    fr = int(input())
    put, blend = map(int, input().split())
    print(int(math.ceil(fr/min(put, blend))))


