def ka(n):
    r = 1
    for i in range(2, n + 1):
        r = r * i
    return r


def ze(n):
    t = 0
    while n > 0:
        t = t + n % 10
        n = n // 10
    return t


def ne(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)


def qa(s):
    t = 0
    for c in s.lower():
        if c in "aeiouy":
            t = t + 1
    return t


def nu(s, c):
    t = 0
    for x in s:
        if x == c:
            t = t + 1
    return t


def po(s, t):
    return sorted(s.lower()) == sorted(t.lower())



def di(s, n):
    if len(s) <= n:
        return s
    return s[:n - 3] + "..."


def su(u, x):
    for i in range(len(u)):
        if u[i] == x:
            return i
    return -1

def mo(s):
    t = 1
    if s >= 2:
        for i in range(1,s):
            t = t * i
    return t
