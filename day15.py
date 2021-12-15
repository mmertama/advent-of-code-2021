import queue

example = '''1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
'''


def djikstra(cave):
    width = len(cave[0])
    height = len(cave)
    start = (0, 0)
    end = (width - 1, height - 1)
    visited = set()
    visited.add(start)

    dists = {start: 0}
    q = queue.PriorityQueue()
    q.put((0, start))

    while not q.empty():
        dist, current = q.get()
        visited.add(current)
        x = current[0]
        y = current[1]

        def neigh(cell):
            if cell in visited:
                return
            dist = cave[cell[1]][cell[0]]
            old_cost = 0xFFFFFFFF if cell not in dists else dists[cell]
            new_cost = dists[current] + dist
            if new_cost < old_cost:
                q.put((new_cost, cell))
                dists[cell] = new_cost

        if x > 0:
            neigh((x - 1, y))
        if y > 0:
            neigh((x, y - 1))
        if x < width - 1:
            neigh((x + 1, y))
        if y < height - 1:
            neigh((x, y + 1))

    return dists[end]


def find_path(data):
    cave = [[int(x) for x in list(ln)] for ln in data]
    distance = djikstra(cave)
    print("Distance:", distance)


def find_path_extended(data):
    cave = [[int(x) for x in list(ln)] for ln in data]
    cave_width = len(cave[0])
    cave_height = len(cave)
    extended = [[0 for x in range(5 * cave_width)] for y in range(5 * cave_height)]

    for j in range(cave_height):
        for i in range(cave_width):
            extended[j][i] = cave[j][i]

    width = len(extended[0])
    height = len(extended)
    for j in range(height):
        for i in range(width):
            if j < cave_height and i < cave_width:
                continue
            v = 0
            if i >= cave_width:
                v = extended[j][i - cave_width]
            if j >= cave_height:
                v = max(v, extended[j - cave_height][i])
            v += 1
            extended[j][i] = 1 if v > 9 else v

    distance = djikstra(extended)
    print("Extended distance:", distance)


