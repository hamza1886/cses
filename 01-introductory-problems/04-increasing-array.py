# https://cses.fi/problemset/hack/1094
n = input()
d = [int(i) for i in input().split(' ')]
t = 0

for i in range(1, len(d)):
    if d[i] < d[i - 1]:
        t += d[i - 1] - d[i]
        d[i] = d[i - 1]
print(t)
