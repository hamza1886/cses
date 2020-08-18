# https://cses.fi/problemset/task/1070
n = int(input())

if n == 1:
    print(n)
    exit()

if n <= 3:
    print('NO SOLUTION')
    exit()

i = 2
while i <= n:
    print(i)
    i += 2

i = 1
while i <= n:
    print(i)
    i += 2
