example='''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
'''


def to_int(bit_list):
    value = 0
    pos = 1
    for b in reversed(bit_list):
        value += int(b) * pos
        pos *= 2
    return value


def power_consumption(data):
    bits = len(data[0])
    gamma_list = []
    epsilon_list = []
    for b in range(0, bits):
        ones = 0
        zeros = 0
        for ln in data:
            byte_list = [char for char in ln]
            assert(len(byte_list) >= 5)
            value = byte_list[b]
            if value == '0':
                zeros += 1
            if value == '1':
                ones += 1
        if ones > zeros:
            gamma_list.append(1)
        else:
            gamma_list.append(0)
        if ones < zeros:
            epsilon_list.append(1)
        else:
            epsilon_list.append(0)
    gamma = to_int(gamma_list)
    epsilon = to_int(epsilon_list)
    pwr = gamma * epsilon
    print("Power consumption:", pwr)


def eliminate(data, bit_pos, eliminator):
    if len(data) == 1:
        return data[0]
    zero_list = []
    ones_list = []
    ones = 0
    zeros = 0
    for ln in data:
        byte_list = [char for char in ln]
        value = byte_list[bit_pos]
        if value == '0':
            zeros += 1
            zero_list.append(ln)
        if value == '1':
            ones += 1
            ones_list.append(ln)
    if eliminator(ones, zeros):
        return eliminate(ones_list, bit_pos + 1, eliminator)
    else:
        return eliminate(zero_list, bit_pos + 1, eliminator)


def life_support(data):
    bits = len(data[0])
    for b in range(0, bits):
        ox_val = eliminate(data, 0, lambda o, z: o >= z)
        co_val = eliminate(data, 0, lambda o, z: o < z)

    oxygen = to_int(ox_val)
    co2 = to_int(co_val)
    life = oxygen * co2
    print("Life support:", life)

