import re


# inp w;mul x 0;add x z;mod x 26;div z ?;
# add x A;
# eql x w;eql x 0;
# mul y 0;add y 25;
# mul y x;add y 1;mul z y;mul y 0;add y w;add y C;mul y x;add z y'''


# a :14 12  11  (-4)    10  10  15  (-9)    (-9)    12  (-15)   (-7)    (-10)   (0)
# c :7  4   8  (1)      5   14  12  (10)    (5)     7   (6)     (8)     (4)     (6)
# do 26 is true only for those, thus only they decrease
# we look  a + (z % 26) == w
# assume all of them has to satisfy, we look the first (a=-4) (4th digit)
# w is 1 - 9, then (z % 26) == (5..13)
# then previous function  (3rd digit) has to return a function that satisfies that one
# (z % 26) == w - a if a 0-9 never goes if a == 11 as then its negative
# z + w + c must satisfy. z % 26 == 0, therefore
# 8 + w must be (5..13) --> w = (5...13) - 8 --> w == (-3...5) --> 3rd digit must be 1..5
# of which we take max (5)

# You can also think that 'what is shifted in, must be shifted out'. Then
# any where z *= 26 happens, must z //= 26.

# a :14 12  11  (-4)    10  10  15  (-9)    (-9)    12  (-15)   (-7)    (-10)   (0)
# c :7  4   8  (1)      5   14  12  (10)    (5)     7   (6)     (8)     (4)     (6)
# z :<0 <1  <2  2>      <2  <3  <4  4>      3>      <3  3>      2>      1>      0>

# Therefore all those 'div z 26', the w has to
# be equal a + (z % 26) == w, meaning, its pair z + (w + c) must provide
# a correct z. E.g. The 14th digit 0 + (z % 26) == (1...9), means
# that the 1st digit z must be 2!
# (0(initial z) + 2(the digit at 1st) + 7(c value, see above)) % 26 == 9 (the digit at 14th)
#  --> the last digit will be reduced!

# a rewritten function so to check output (see the return None)
def function2(w, z, do26, a, c):
    if a + (z % 26) == w:
        return z // 26 if do26 else z
    elif do26:
        return None
    if do26:
        z //= 26
    return (z * 26) + w + c


# 'universal' param parsing
def get_params(data):
    parts = []
    for d in data:
        if 'inp' in d:
            parts.append([])
        parts[-1].append(d)
    params = []
    for p in parts:
        ln = ';'.join(p)
        pattern = r'inp\sw;mul\sx\s0;add\sx\sz;mod\sx\s26;div\sz\s((?:26)|1);add\sx\s(-?\d+);eql\sx\sw;eql\sx\s0;mul\sy\s0;add\sy\s25;mul y x;add y 1;mul z y;mul y 0;add\sy\sw;add\sy\s(-?\d+);mul\sy\sx;add\sz\sy'
        m = re.match(pattern, ln)
        assert m
        params.append((
            (True if m.group(1) == '26' else False), int(m.group(2)), int(m.group(3))))
    return params


def monad_min(data):
    params = get_params(data)
    inputs = [int(x) for x in list(str(11111111111111))]

    def calc(z, i):
        while inputs[i] < 10:
            z0 = function2(inputs[i], z, params[i][0], params[i][1], params[i][2])
            if z0 is not None:      # value ok
                if i == 13:         # all ok
                    return z0
                z1 = calc(z0, i + 1)    # calc next
                if z1 is None:          # if next was not ok
                    inputs[i] += 1      # we try one more
                else:
                    return z1
            else:
                # loop this, actually the function2, could return the correct input directly to
                # be faster, but this is ok now
                inputs[i] += 1
        inputs[i] = 1       # reset the looped value if we loop one above
        return None

    zz = calc(0, 0)
    assert zz == 0
    x = ''.join([str(x) for x in inputs])
    print("MONAD min:", int(x))


def monad_max(data):
    params = get_params(data)
    inputs = [int(x) for x in list(str(99999999999999))]

    def calc(z, i):
        while inputs[i] > 0:
            z0 = function2(inputs[i], z, params[i][0], params[i][1], params[i][2])
            if z0 is not None:
                if i == 13:
                    return z0
                z1 = calc(z0, i + 1)
                if z1 is None:
                    inputs[i] -= 1
                else:
                    return z1
            else:
                inputs[i] -= 1
        inputs[i] = 9
        return None

    zz = calc(0, 0)
    assert zz == 0
    x = ''.join([str(x) for x in inputs])
    print("MONAD max:", int(x))


def execute0b(inputs):

    def function1(w, z, do26, a, c):
        x = 0
        x *= 0
        x += z
        x %= 26
        z //= 26 if do26 else 1
        x += a
        x = 1 if x == w else 0
        x = 1 if x == 0 else 0
        y = 0
        y += 25
        y *= x
        y += 1
        z = z * y
        y *= 0
        y += w
        y += c
        y *= x
        z += y
        return z

    z = function1(inputs.pop(0), 0, False, 14, 7)
    z = function1(inputs.pop(0), z, False, 12, 4)
    z = function1(inputs.pop(0), z, False, 11, 8)
    z = function1(inputs.pop(0), z, True, -4, 1)
    z = function1(inputs.pop(0), z, False, 10, 5)
    z = function1(inputs.pop(0), z, False, 10, 14)
    z = function1(inputs.pop(0), z, False, 15, 12)
    z = function1(inputs.pop(0), z, True, -9, 10)
    z = function1(inputs.pop(0), z, True, -9, 5)
    z = function1(inputs.pop(0), z, False, 12, 7)
    z = function1(inputs.pop(0), z, True, -15, 6)
    z = function1(inputs.pop(0), z, True, -7, 8)
    z = function1(inputs.pop(0), z, True, -10, 4)
    return function1(inputs.pop(0), z, True, 0, 6)


def execute0(inputs, lines):
    vars = {'x': 0, 'y': 0, 'z': 0, 'w': 0}
    for inst in lines:
        op = inst[0]
        pk = inst[1]
        if op == 'inp':
            input_value = inputs.pop(0)
            vars[pk] = input_value
            continue
        if pk[0].isalpha():
            p1 = vars[pk]
        else:
            p1 = int(pk)
        p2 = inst[2]
        if p2 in vars:
            p2 = vars[p2]
        else:
            p2 = int(p2)

        if op == 'add':
            vars[pk] = p1 + p2
            continue
        if op == 'mul':
            vars[pk] = p1 * p2
            continue
        if op == 'div':
            vars[pk] = p1 // p2
            continue
        if op == 'mod':
            vars[pk] = p1 % p2
            continue
        if op == 'eql':
            vars[pk] = 1 if p1 == p2 else 0
            continue
        assert False
    return vars
