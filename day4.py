import re


example = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
 '''

BINGO_SZ = 5


def read_bingo(data):
    numbers = [int(x) for x in data[0].split(',')]
    tables = []
    table = []
    for ln in data:
        if re.match(r'\s*$', ln):
            if len(table) > 0:
                tables.append(table)
            table = []
        m = re.match(r'\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)', ln)
        if m:
            table.append([(int(m.group(x)), False) for x in range(1, BINGO_SZ + 1)])
    if len(table) > 0:
        tables.append(table)
    return numbers, tables


def find(value, table):
    r = 0
    c = 0
    for row in range(BINGO_SZ):
        for col in range(BINGO_SZ):
            if table[row][col][0] == value:
                count_r = 0
                count_c = 0
                table[row][col] = (value, True)
                for i in range(BINGO_SZ):
                    if table[row][i][1]:
                        count_r += 1
                    if table[i][col][1]:
                        count_c += 1
                return count_c == BINGO_SZ or count_r == BINGO_SZ
    return False


def sum_unmarked(table):
    summa = 0
    for row in range(BINGO_SZ):
        for col in range(BINGO_SZ):
            if not table[row][col][1]:
                summa += table[row][col][0]
    return summa


def play_bingo(data):
    numbers, tables = read_bingo(data)
    for n in numbers:
        for t in tables:
            if find(n, t):
                s = sum_unmarked(t)
                print("Bingo:", s * n)
                return


def reset(tables):
    for table in tables:
        for row in range(BINGO_SZ):
            for col in range(BINGO_SZ):
                if table[row][col][1]:
                    table[row][col] = (table[row][col][0], False)


def play_last_bingo(data):
    numbers, tables = read_bingo(data)
    while True:
        index = 0
        for n in numbers:
            index += 1
            for t in tables:
                if find(n, t):
                    last_number = n
                    if len(tables) == 1:
                        s = sum_unmarked(tables[0])
                        print("Last Bingo:", s * last_number)
                        return
                    tables.remove(t)
                    reset(tables)
                    break
            else:
                continue
            break

