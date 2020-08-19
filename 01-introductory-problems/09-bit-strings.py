# https://cses.fi/problemset/task/1617
n = int(input())
m = 1e9 + 7
r = 1

for _ in range(n):
    r = r * 2 % m

print(int(r))
