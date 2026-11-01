def qa(s):
    t = 0
    for c in s.lower():
        if c in "aeiouy":
            t = t + 1
    return t


def wi(s):
    u = s.lower().replace(" ", "")
    return u == u[::-1]


def lo(s):
    m = s.split(" ")
    r = []
    for x in m:
        r.append(x.capitalize())
    return " ".join(r)


def nu(s, c):
    t = 0
    for x in s:
        if x == c:
            t = t + 1
    return t


def fu(s):
    if s == "":
        return ""
    r = ""
    c = s[0]
    t = 1
    for x in s[1:]:
        if x == c:
            t = t + 1
        else:
            r = r + c + str(t)
            c = x
            t = 1
    return r + c + str(t)


def ta(s, k):
    r = ""
    for c in s:
        if "a" <= c <= "z":
            r = r + chr((ord(c) - ord("a") + k) % 26 + ord("a"))
        else:
            r = r + c
    return r


def ri(s):
    m = 0
    for x in s.split():
        if len(x) > m:
            m = len(x)
    return m


def po(s, t):
    return sorted(s.lower()) == sorted(t.lower())


def ju(s):
    d = {}
    for c in s:
        if c.isalpha():
            c = c.lower()
            if c in d:
                d[c] = d[c] + 1
            else:
                d[c] = 1
    return d


def di(s, n):
    if len(s) <= n:
        return s
    return s[:n - 3] + "..."
