t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    
    for _ in range(m):
        s = input()
        
        if len(s) != n:
            print("NO")
            continue
        
        valid = True
        map_int_to_char = {}
        map_char_to_int = {}
        
        for i in range(n):
            if a[i] in map_int_to_char:
                if map_int_to_char[a[i]] != s[i]:
                    valid = False
                    break
            else:
                map_int_to_char[a[i]] = s[i]
            
            if s[i] in map_char_to_int:
                if map_char_to_int[s[i]] != a[i]:
                    valid = False
                    break
            else:
                map_char_to_int[s[i]] = a[i]
        
        if valid:
            print("YES")
        else:
            print("NO")

