# https://cses.fi/problemset/task/1069
s, st, p_st, n = input(), '', '', 0

for c in s:
    if st and c == st[-1]:
        st += c
        n += 1
    else:
        if len(st) > len(p_st): p_st = st
        st, n = c, 1

x = len(st)
y = len(p_st)
print(x if x > y else y)
