# https://cses.fi/problemset/task/1083
d = [False for _ in range(int(input()))]

for i in input().split(' '):
    d[int(i) - 1] = True

for i, b in enumerate(d):
    if not b:
        print(i + 1)
        exit()
