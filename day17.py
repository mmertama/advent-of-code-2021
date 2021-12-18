import re

example = '''target area: x=20..30, y=-10..-5'''
input_1 = '''target area: x=117..164, y=-140..-89'''


def parse_target(line):
    m = re.match(r'target\sarea:\sx=(-?\d+)..(-?\d+),\sy=(-?\d+)..(-?\d+)',
                 line)
    assert m
    x = (int(m.group(1)), int(m.group(2)))
    y = (int(m.group(3)), int(m.group(4)))
    return x, y


def calc_trajectory_high(target_x, target_y):
    # we are only concern how to hit the area.
    # the top speed is the top point and the lower we get
    # the better. So what is top point from the  lowest point of area?
    # speed at top is 0 then we speed up 1 + 2 +
    # thus the travelled distance is sum(1...abs(target))
    sum = 0
    for i in range(0, abs(target_y[0])):
        sum += i
    return sum


def trajectory_high(line):
    target_x, target_y = parse_target(line)
    maxima = calc_trajectory_high(target_x, target_y)
    print("Maxima:", maxima)


def count_trajectory(line):
    target_x, target_y = parse_target(line)
    maxima = calc_trajectory_high(target_x, target_y)
    sy_min = target_y[0]   # left edge
    sy_max = -target_y[0]  # hmm what is this rationale, I assume this is the top related position discussed with #1 (aka good guess :-)
    sx_min = 1             # just do loop from here
    sx_max = target_x[1]   # back edge
    success = 0

    tx0 = target_x[0]
    tx1 = target_x[1]
    ty0 = target_y[0]
    ty1 = target_y[1]

    def calc_trajectory(v_x, v_y):
        p_x = 0
        p_y = 0
        while True:
            if p_y < ty0:
                return None, None
            if ty0 <= p_y <= ty1 and tx0 <= p_x <= tx1:
                return p_x, p_y
            p_x += v_x
            p_y += v_y

            if p_x > tx1:
                return None, None

            if v_x > 0:
                v_x -= 1
            v_y -= 1

    for sy in range(sy_min, sy_max + 1):
        for sx in range(sx_min, sx_max + 1):
            x, y = calc_trajectory(sx, sy)
            if x and y:
                success += 1

    print("Brute force tells count trajectory:", success)
