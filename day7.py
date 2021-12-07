import math

example = '''16,1,2,0,4,2,7,1,2,14'''


def align_submarines(data):
    positions = sorted([int(x) for x in data[0].split(',')])
    median = positions[int(0.5 + len(positions) / 2.)]
    consumption = 0
    for p in positions:
        consumption += abs(median - p)
    print("Consumption:", consumption)


def align_submarines_bad(data):
    positions = sorted([int(x) for x in data[0].split(',')])
    median = positions[int(0.5 + len(positions) / 2.)]
    consumption = 0
    for p in positions:
        d = abs(median - p)
        s = (d * (d + 1)) / 2  # https://en.wikipedia.org/wiki/Triangular_number
        consumption += int(s)
    print("Consumption bad:", consumption)


def align_submarines_x2(data):
    positions = sorted([int(x) for x in data[0].split(',')])
    min_consumption = 0xFFFFFFFF
    for at in range(positions[0], positions[-1]):
        consumption = 0
        for p in positions:
            d = abs(at - p)
            s = (d * (d + 1)) / 2  # https://en.wikipedia.org/wiki/Triangular_number
            consumption += int(s)
        if consumption < min_consumption:
            min_consumption = consumption
    print("Consumption x2:", min_consumption)





