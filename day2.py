import re


example = '''forward 5
down 5
forward 8
up 3
down 8
forward 2
'''


def navigate(data):
    advance = 0
    depth = 0
    for ln in data:
        m = re.match(r'(.+)\s+(\d+)', ln)
        assert m
        cmd = m.group(1)
        value = int(m.group(2))
        if cmd == 'forward':
            advance += value
        elif cmd == 'down':
            depth += value
        elif cmd == 'up':
            depth -= value
        else:
            assert False
    pos = advance * depth
    print('Navigated:', pos)


def navigate_aim(data):
    advance = 0
    depth = 0
    aim = 0
    for ln in data:
        m = re.match(r'(.+)\s+(\d+)', ln)
        assert m
        cmd = m.group(1)
        value = int(m.group(2))
        if cmd == 'forward':
            advance += value
            depth += aim * value
        elif cmd == 'down':
            aim += value
        elif cmd == 'up':
            aim -= value
        else:
            assert False
    pos = advance * depth
    print('Navigated:', pos)
