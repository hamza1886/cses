# https://cses.fi/problemset/task/1618
def zeros(n):
    return 0 if n < 5 else zeros(n // 5) + n // 5


print(zeros(int(input())))
