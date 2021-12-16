import math

example0 = '''D2FE28
38006F45291200
EE00D40C823060
8A004A801A8002F478
620080001611562C8802118E34
C0015000016115A2E0802F182340
A0016C880162017C3686B18A3D4780
'''

example1 = '''C200B40A82
04005AC33890
880086C3E88112
CE00C43D881120
D8005AC2A8F0
F600BC2D8F
9C005AC2F8F0
9C0141080250320F1802104A08
'''


def split_bits(data):
    bit_array = []
    hex_values = list(data)
    for h in hex_values:
        v = bin(int(h, 16))
        bits = str(v)[2:].zfill(4)  # padding
        bit_array.extend(list(bits))
    return bit_array


def get(bits, at, count):
    bit_str = ''.join(bits)[at: at + count]
    return int(bit_str, 2)


def parse_bits(bits):
    type_id = get(bits, 3, 3)
    if type_id == 4:
        pos = 6
        decimal = 0
        while True:
            prefix = get(bits, pos, 1)
            pos += 1
            decimal <<= 4
            group = get(bits, pos, 4)
            pos += 4
            decimal += group
            if prefix == 0:
                break
        packet_ver = get(bits, 0, 3)
        return packet_ver, pos, decimal
    else:
        return operator(bits)


def operator(bits):
    length_type_id = get(bits, 6, 1)
    version_sum = get(bits, 0, 3)
    type_id = get(bits, 3, 3)
    elapsed_len = 0
    values = []
    if length_type_id == 0:
        sub_len = get(bits, 7, 15)
        while elapsed_len < sub_len:
            p_v, p_l, v = parse_bits(bits[22 + elapsed_len:])
            values.append(v)
            version_sum += p_v
            elapsed_len += p_l
        elapsed_len += 22
    else:
        sub_count = get(bits, 7, 11)
        for _ in range(sub_count):
            p_v, p_l, v = parse_bits(bits[18 + elapsed_len:])
            values.append(v)
            version_sum += p_v
            elapsed_len += p_l
        elapsed_len += 18
    if type_id == 0:
        result = sum(values)
    if type_id == 1:
        result = math.prod(values)
    if type_id == 2:
        result = min(values)
    if type_id == 3:
        result = max(values)
    if type_id == 5:
        result = 1 if values[0] > values[1] else 0
    if type_id == 6:
        result = 1 if values[0] < values[1] else 0
    if type_id == 7:
        result = 1 if values[0] == values[1] else 0
    return version_sum, elapsed_len, result


def parse_transmissions(data):
    for ln in data:
        bits = split_bits(ln)
        ver_sum, _, _ = parse_bits(bits)
        print("version sum: ", ver_sum)


def calc_transmissions(data):
    for ln in data:
        bits = split_bits(ln)
        _, _, result = parse_bits(bits)
        print("Result: ", result)

