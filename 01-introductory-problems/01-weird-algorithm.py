# https://cses.fi/problemset/task/1068
n = int(input())
print(n)

while n != 1:
    n = n // 2 if n % 2 == 0 else 3 * n + 1
    print(n)
