def ka(n):
    r = 1
    for i in range(2, n + 1):
        r = r * i
    return r


def mo(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def vi(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True


def ze(n):
    t = 0
    while n > 0:
        t = t + n % 10
        n = n // 10
    return t


def pu(a, b):
    return a * b // mo(a, b)


def ru(n):
    t = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        t = t + 1
    return t


def te(n):
    u = []
    for i in range(1, n + 1):
        if n % i == 0:
            u.append(i)
    return u


def li(n):
    return sum(te(n)) - n == n


def xa(n):
    r = 0
    while n > 0:
        r = r * 10 + n % 10
        n = n // 10
    return r


def ne(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)
