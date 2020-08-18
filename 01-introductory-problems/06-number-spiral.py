# https://cses.fi/problemset/task/1071
def pos(r, c):
    m = max(r, c)
    s = m * m - m + 1
    if r == c: return s
    if r % 2 == 0 and c % 2 == 0: return s - (m - r) if r < c else s + (m - c)
    if r % 2 == 0 and c % 2 != 0: return s + (m - r) if r < c else s + (m - c)
    if r % 2 != 0 and c % 2 != 0: return s + (m - r) if r < c else s - (m - c)
    if r % 2 != 0 and c % 2 == 0: return s - (m - r) if r < c else s - (m - c)


n, d = int(input()), []
for _ in range(n):
    r, c = input().split(' ')
    d.append(pos(int(r), int(c)))
for i in d:
    print(i)
