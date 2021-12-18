import re

example = '''[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]'''


def parse_number(num_str):
    values = []
    i = 1
    while i < len(num_str):
        n = num_str[i]
        if n == '[':
            sub, consumed = parse_number(num_str[i:])
            values.append(sub)
            i += consumed
            continue
        if n == ']':
            return values, i + 1
        if n != ',':
            e = i + 1
            while '0' <= num_str[e] <= '9':
                e += 1
            values.append(int(num_str[i: e]))
            i = e - 1
        i += 1


def explode(number):
    depth = 0
    for i in range(len(number)):
        if number[i] == '[':
            depth += 1
        if number[i] == ']':
            depth -= 1
        if depth > 4:
            e = explode_number(number, i)
            return e
    return number


# after HOURS of trying to get the value-tree version doing right I gave
# up and get to the regexp, doing explosion as a string!
def explode_number(number, from_position):
    m = re.search(r'\[(\d+),(\d+)\]', number[from_position:])
    assert m
    s = m.span()
    span = (s[0] + from_position, s[1] + from_position)
    left = number[:span[0]]
    prev_m = re.search(r'\d+(?!.*\d)', left)
    if prev_m:
        pspan = prev_m.span()
        ex = left[:pspan[0]]
        ex += str(int(m.group(1)) + int(prev_m.group(0)))
        ex += left[pspan[1]:]
    else:
        ex = left
    ex += '0'
    right = number[span[1]:]
    next_m = re.search(r'(\d+)', right)
    if next_m:
        nspan = next_m.span()
        ex += right[:nspan[0]]
        ex += str(int(m.group(2)) + int(next_m.group(0)))
        ex += right[nspan[1]:]
    else:
        ex += right
    return ex


def splitted(number):
    if type(number) is int:
        if number > 9:
            number /= 2.
            return [int(number), int(number + .5)], True
        else:
            return number, False
    left = number[0]
    right = number[1]
    left, is_split = splitted(left)
    if not is_split:
        right, is_split = splitted(right)
    return [left, right], is_split


def split(number):
    tree, l = parse_number(number)
    s, is_split = splitted(tree)
    return str(s).replace(' ', '')


def add(a, b):
    value = '[' + a + ',' + b + ']'
    while True:
        exp = explode(value)
        is_action = value != exp
        if is_action:
            value = exp
            continue
        value = split(exp)
        is_action = is_action or value != exp
        if not is_action:
            return value


def calc_mag(number):
    if type(number) is int:
        return number
    return 3 * calc_mag(number[0]) + 2 * calc_mag(number[1])


def magnitude(number):
    no, _ = parse_number(number)
    return calc_mag(no)


def snail_fish_magnitude(data):
    value = None
    for ln in data:
        if not value:
            value = ln
        else:
            value = add(value, ln)

    print("Snailfish magnitude:", magnitude(value))


def largest_snail_fish_magnitude(data):
    maximum = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            r = magnitude(add(data[i], data[j]))
            if r > maximum:
                maximum = r
            r = magnitude(add(data[j], data[i]))
            if r > maximum:
                maximum = r
    print("Maximum magnitude", maximum)
