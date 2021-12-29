example = '''v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>'''


def parse(data):
    sm = []
    for ln in data:
        sm.append(list(ln))
    return sm


def step(sea_map):
    height = len(sea_map)
    width = len(sea_map[0])
    next_map0 = [['.' for _ in range(0, width)] for _ in range(0, height)]
    for r in range(height):
        for c in range(width):
            current = sea_map[r][c]
            if current == '.':
                continue
            if current == '>':
                col = c + 1 if c < width - 1 else 0
                if sea_map[r][col] == '.':
                    next_map0[r][col] = '>'
                else:
                    next_map0[r][c] = current
            if current == 'v':
                next_map0[r][c] = current
    sea_map = next_map0
    next_map1 = [['.' for _ in range(0, width)] for _ in range(0, height)]
    for r in range(height):
        row = r + 1 if r < height - 1 else 0
        for c in range(width):
            current = sea_map[r][c]
            if current == 'v':
                if sea_map[row][c] == '.':
                    next_map1[row][c] = 'v'
                else:
                    next_map1[r][c] = current
            if current == '>':
                next_map1[r][c] = current
    sea_map = next_map1
    return sea_map


def sea_cucumber_stop(data):
    sea_map = parse(data)
    steps = 0
    while True:
        steps += 1
        # for ln in sea_map:
        #    print(''.join(ln))
        sea_map0 = step(sea_map)
        if sea_map == sea_map0:
            break
        sea_map = sea_map0
    print("steps: ", steps)
