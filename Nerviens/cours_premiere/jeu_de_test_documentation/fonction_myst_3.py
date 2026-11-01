def ba(u):
    if len(u) == 0:
        return None
    t = 0
    for x in u:
        t = t + x
    return t / len(u)


def co(u):
    if len(u) == 0:
        return None
    m = u[0]
    for x in u:
        if x > m:
            m = x
    return m


def su(u, x):
    for i in range(len(u)):
        if u[i] == x:
            return i
    return -1


def de(u):
    r = []
    for x in u:
        if x not in r:
            r.append(x)
    return r


def mi(u):
    a = u[0]
    b = u[0]
    for x in u:
        if x < a:
            a = x
        if x > b:
            b = x
    return (a, b)


def fa(u):
    if len(u) > 1:
        u[0], u[-1] = u[-1], u[0]


def tu(u, k):
    return [x for x in u if x > k]


def ha(u, v):
    r = []
    i = 0
    j = 0
    while i < len(u) and j < len(v):
        if u[i] <= v[j]:
            r.append(u[i])
            i = i + 1
        else:
            r.append(v[j])
            j = j + 1
    return r + u[i:] + v[j:]


def no(u):
    d = {}
    for x in u:
        d[x] = d.get(x, 0) + 1
    return d


def ge(m):
    r = []
    for j in range(len(m[0])):
        t = []
        for i in range(len(m)):
            t.append(m[i][j])
        r.append(t)
    return r
