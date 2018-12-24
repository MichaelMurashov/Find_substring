import time


def naive(text, pattern):
    start = time.time()

    n = len(text)
    m = len(pattern)

    res_pos = []

    for i in range(n - m - 1):
        if text[i:(i+m)] == pattern:
            res_pos.append(i)

    stop = time.time()
    return res_pos, stop - start


def rabin_karp(text, pattern, d, q):

    n = len(text)
    m = len(pattern)
    p = 0
    t = 0

    result = []

    h = pow(d, m - 1) % q
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q

    start = time.time()

    for s in range(n - m + 1):
        if p == t:
            if text[s:s+m] == pattern:
                result.append(s)

        if s < n - m:
            t = (d * (t-ord(text[s])*h) + ord(text[s+m])) % q

    stop = time.time()
    return result, stop - start


def rb1(text, pattern, d):
    pows = [1]
    for i in range(1, len(text)):
        pows.append(pows[i - 1] * d)


def get_prefixs(pattern):
    m = len(pattern)
    pi = [0]

    for i in range(1, m):
        k = pi[i - 1]
        while k > 0 and pattern[k] != pattern[i]:
            k = pi[k - 1]
        if pattern[k] == pattern[i]:
            k += 1
        pi.append(k)

    return pi


def kmp(text, pattern):
    start = time.time()

    n = len(text)
    m = len(pattern)
    q = 0
    results = []

    pi = get_prefixs(pattern)

    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q]
        if pattern[q] == text[i]:
            q += 1
        if q == m:
            results.append(i - m + 1)
            q = pi[q - 1]

    stop = time.time()
    return results, stop - start
