
example = '''2199943210
3987894921
9856789892
8767896789
9899965678'''


def get_height_map(data):
    height_map = []
    width = len(data[0])
    height = len(data)
    for ln in data:
        height_map.append([int(x) for x in list(ln.rstrip())])
    min_list = []
    for y in range(height):
        for x in range(width):
            current = height_map[y][x]
            m_count = 0
            if y == 0 or height_map[y - 1][x] > current:
                m_count += 1
            if x == 0 or height_map[y][x - 1] > current:
                m_count += 1
            if y >= height - 1 or height_map[y + 1][x] > current:
                m_count += 1
            if x >= width - 1 or height_map[y][x + 1] > current:
                m_count += 1
            if m_count == 4:
                min_list.append((x, y))
    return height_map, min_list, width, height


def risk_level_sum(data):
    height_map, min_list, _, _ = get_height_map(data)
    risk_level = 0
    for m in min_list:
        risk_level += height_map[m[1]][m[0]] + 1
    print("Risk level:", risk_level)


def get_basins(x, y, height_map, width, height):
    current = height_map[y][x]
    height_map[y][x] = current + 10
    basins = [(x, y)]
    if x > 0 and height_map[y][x - 1] < 9:
        basins.extend(get_basins(x - 1, y, height_map, width, height))
    if y > 0 and height_map[y - 1][x] < 9:
        basins.extend(get_basins(x, y - 1, height_map, width, height))
    if x < width - 1 and height_map[y][x + 1] < 9:
        basins.extend(get_basins(x + 1, y, height_map, width, height))
    if y < height - 1 and height_map[y + 1][x] < 9:
        basins.extend(get_basins(x, y + 1, height_map, width, height))
    return basins


def basin_top_mul(data):
    height_map, min_list, width, height = get_height_map(data)
    basins = []
    for m in min_list:
        basins.append(get_basins(m[0], m[1], height_map, width, height))
    basins.sort(key=len, reverse=True)
    top = len(basins[0]) * len(basins[1]) * len(basins[2])
    print("Top 3", top)


