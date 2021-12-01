example = '''199
200
208
210
200
207
240
269
260
263
'''


def count_ascent(data_lines):
    prev = 0xFFFFFFFF
    count = 0
    for ln in data_lines:
        current = int(ln)
        if current > prev:
            count += 1
        prev = current
    print("Ascents:" + str(count))


def count_ascent_sliding_window(data_lines):
    prev2 = int(data_lines[1])
    prev3 = int(data_lines[2])
    count = 0
    prev = int(data_lines[0]) + prev2 + prev3
    for i in range(3, len(data_lines)):
        value = int(data_lines[i])
        summa = prev2 + prev3 + value
        if summa > prev:
            count += 1
        prev2 = prev3
        prev3 = value
        prev = summa
    print("Ascents:" + str(count))
