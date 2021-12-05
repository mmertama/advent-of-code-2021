import re

example='''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
'''


def line(data):
    m = re.match(r'(\d+),(\d+)\s->\s(\d+),(\d+)', data)
    assert m, data
    return (int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))


def line_overlap(data, do_all):
    points = {}
    for ln in data:
        s, e = line(ln)
        if not do_all and not (s[0] == e[0] or s[1] == e[1]):
            continue
        inc0 = 1 if s[0] < e[0] else -1
        inc1 = 1 if s[1] < e[1] else -1
        p0 = s[0]
        p1 = s[1]
        h = (p0 << 16) + p1
        if h in points:
            points[h] += 1
        else:
            points[h] = 1
        while p0 != e[0] or p1 != e[1]:
            if p0 != e[0]:
                p0 += inc0
            if p1 != e[1]:
                p1 += inc1
            h = (p0 << 16) + p1
            if h in points:
                points[h] += 1
            else:
                points[h] = 1
    joints = 0
    for p in points:
        if points[p] > 1:
            joints += 1
    print("Joints:", joints)


def line_overlap_orthogonal(data):
    line_overlap(data, False)


def line_overlap_all(data):
    line_overlap(data, True)

