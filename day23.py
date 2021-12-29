from copy import deepcopy

example = '''#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########'''

example2 = '''#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########'''

input_data = '''#############
#...........#
###B#B#D#A###
  #D#C#A#C#
  #########'''

input_data2 = '''#############
#...........#
###B#B#D#A###
  #D#C#B#A#
  #D#B#A#C#
  #D#C#A#C#
  #########'''

MOVE_COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}


def print_burrow(burrow, hallway, depth):
    print('#############')
    print('#' + ''.join([x if x else '.' for x in hallway]) + '#')
    for d in range(depth):
        print('  #' + '#'.join(c[d] if c[d] else '.' for c in burrow) + '#')
    print('  #########')


min_cost = 99999999


def organize(burrow, hallway, cost, depth):
    global min_cost

    cave_mounts = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
    hallway_free = [0, 1, 3, 5, 7, 9, 10]

    def to_caves():
        nonlocal cost
        for hallway_pos, amphipod in enumerate(hallway):
            amphipod = hallway[hallway_pos]
            if amphipod:
                mount_pos = cave_mounts[amphipod]
                path = hallway[mount_pos:hallway_pos - 1] if hallway_pos > mount_pos else hallway[hallway_pos + 1:mount_pos]
                if not any(path):
                    cave = ord(amphipod) - ord('A')
                    cave_pos = None
                    for d in range(depth - 1, -1, -1):
                        if not burrow[cave][d] and not cave_pos:
                            cave_pos = d
                        if burrow[cave][d] and burrow[cave][d] != amphipod:
                            break
                    if cave_pos is not None:
                        burrow[cave][cave_pos] = amphipod
                        hallway[hallway_pos] = None
                        cost += (len(path) + cave_pos + 1) * MOVE_COST[amphipod]
                        return True
        return False

    if cost > min_cost:
        return None

    while to_caves():
        if all([all([burrow[x][y] == chr(ord('A') + x) for y in range(depth)]) for x in
                range(0, len(burrow))]):
            if cost < min_cost:
                min_cost = cost

    def to_hallway(cave_index, cave_pos):
        nonlocal cost
        mount_pos = (cave_index + 1) * 2
        cave = burrow[cave_index]
        amphipod = cave[cave_pos]
        if amphipod:
            in_own_cave = ord(amphipod) - ord('A') == cave_index
            for c in range(len(cave)):
                if c < cave_pos and cave[c]:
                    return  # wont go
                if c > cave_pos and ord(cave[c]) - ord('A') != cave_index:
                    in_own_cave = False
            if in_own_cave:
                return
            for hallway_pos in hallway_free:
                path = hallway[min(hallway_pos, mount_pos):max(hallway_pos, mount_pos) + 1]
                if not any(path):
                    sub_cost = (len(path) + cave_pos + 1) * MOVE_COST[amphipod]
                    new_burrow = deepcopy(burrow)
                    new_hallway = deepcopy(hallway)
                    new_hallway[hallway_pos] = burrow[cave_index][cave_pos]
                    new_burrow[cave_index][cave_pos] = None
                    organize(new_burrow, new_hallway, cost + sub_cost, depth)

    for index in range(len(burrow)):
        for pos in range(depth):
            to_hallway(index, pos)


def organize_amphipods(data):
    global min_cost
    min_cost = 99999999
    hallway = [None] * 11
    burrow = [[data[2][3], data[3][3]],
              [data[2][5], data[3][5]],
              [data[2][7], data[3][7]],
              [data[2][9], data[3][9]]]

    organize(burrow, hallway, 0, 2)
    print("Organize cost is", min_cost)


def organize_amphipods_unfolded(data):
    global min_cost
    min_cost = 99999999
    hallway = [None] * 11
    burrow = [[data[2][3], data[3][3], data[4][3], data[5][3]],
              [data[2][5], data[3][5], data[4][5], data[5][5]],
              [data[2][7], data[3][7], data[4][7], data[5][7]],
              [data[2][9], data[3][9], data[4][9], data[5][9]]]

    organize(burrow, hallway, 0, 4)
    print("Organize cost is", min_cost)

