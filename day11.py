import copy

example = '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
'''

example0 = '''11111
19991
19191
19991
11111
'''


def octopus_flashes(data, steps, stop_on_sync):
    grid = []
    for fn in data:
        grid.append([int(x) for x in list(fn)])
    height = len(grid)
    width = len(grid)
    all_flash = 0
    for at in range(steps):
        while True:
            flashes = 0
            grid_next = copy.deepcopy(grid)
            for c in range(height):
                for r in range(width):
                    if grid[c][r] == 9:
                        flashes += 1
                        for cc in range(max(0, c - 1), min(height - 1, c + 1) + 1):
                            for rr in range(max(0, r - 1), min(width - 1, r + 1) + 1):
                                if (cc == c and rr == r) or grid_next[cc][rr] < 9:  # > 9 means it has flashed, but not yet...
                                    grid_next[cc][rr] += 1
            grid = copy.deepcopy(grid_next)
            if flashes == 0:
                break

        total_flashes = 0
        for c in range(height):
            for r in range(width):
                if grid[c][r] > 9:
                    grid[c][r] = 0
                    total_flashes += 1
                else:
                    grid[c][r] += 1
        all_flash += total_flashes
        if stop_on_sync and total_flashes == width * height:
            break
    return all_flash, at + 1


def octopus_flash_count(data, steps=100):
    flashes, _ = octopus_flashes(data, steps, False)
    print(flashes, "flashes after", steps)


def octopus_all_flash(data, steps=100000):
    _, at = octopus_flashes(data, steps, True)
    print("Sync at", at)









