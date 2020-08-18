# https://cses.fi/problemset/task/1072
n = int(input())
for k in range(1, n + 1):
    print(int(k * k * (k * k - 1) / 2 - (k - 1) * (k - 2) * 4))
