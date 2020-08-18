# https://cses.fi/problemset/task/1092
n = int(input())
if n % 4 in [1, 2]:
    print('NO')
    exit()

s1, s2 = '', ''
if n % 4 == 0:
    x = n // 2 + 1
    for i in range(1, x, 2):
        s1 += str(i) + ' ' + str(n - i + 1) + ' '
        s2 += str(i + 1) + ' ' + str(n - i) + ' '
else:
    s1 = '1 2'
    s2 = '3'
    for i in range(4, n, 4):
        s1 += ' ' + str(i) + ' ' + str(i + 3)
        s2 += ' ' + str(i + 1) + ' ' + str(i + 2)

print('YES')
print((n + 1) // 2)
print(s1)
print(n // 2)
print(s2)
