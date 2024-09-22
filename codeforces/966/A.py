t = int(input())
for _ in range(t):
    s = input().strip()
    if s.startswith('10'):
        x_str = s[2:]
        if x_str and x_str[0] != '0' and x_str.isdigit() and int(x_str) >= 2:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')

