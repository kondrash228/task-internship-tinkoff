n = int(input())

a = 1
b = 1


def next_decomp(n, inp, res):
    if len(inp) == 0:
        return res
    else:
        iinp = []
        rres = res
        for z in inp:
            sz = sum(z)
            if sz == n:
                zz = sorted(z)
                if not zz in rres:
                    rres.append(zz)
            else:
                k = n - sz
                for i in range(1, k + 1):
                    iinp.append([i] + z)
        return next_decomp(n, iinp, rres)


def gen_sum(n):
    res = []
    for a in next_decomp(n, [[i] for i in range(1, n + 1)], []):
        res.append(list(reversed(a)))
    return sorted(res, reverse=True)


def lcm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return (m // (a + b))


all_decomps = gen_sum(n)
min_nok = lcm(all_decomps[0][0], all_decomps[0][-1])
a_min = 0
b_min = 0

for i in range(len(all_decomps)):
    for j in range(len(all_decomps[i])):
        if len(all_decomps[i]) == 2:
            if lcm(all_decomps[i][0], all_decomps[i][-1]) <= min_nok and all_decomps[i][0] + all_decomps[i][-1] == n:
                a_min = all_decomps[i][0]
                b_min = all_decomps[i][-1]

print(a_min, b_min)
