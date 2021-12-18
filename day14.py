import re
from collections import Counter
example = '''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
'''


def parse_polymers(data):
    pol = None
    inst = {}
    for ln in data:
        if len(ln) == 0:
            continue
        m = re.match(r'[A-Z]+$', ln)
        if m:
            pol = m.group(0)
            continue
        m = re.match(r'([A-Z]+)\s*->\s*([A-Z])', ln)
        if m:
            inst[m.group(1)] =  m.group(2)

    return pol, inst


def count(polymer):
    counter = {}
    for c in polymer:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1
    return counter


def find_polymers0(data, steps):
    polymer, instructions = parse_polymers(data)
    for i in range(steps):
        inject_pos = 0

        def loop(pos):
            nonlocal polymer
            nonlocal inject_pos
            for inst, val in instructions.items():
                if inst == polymer[pos:pos + 2]:
                    polymer = polymer[:pos + 1] + val + polymer[pos + 1:]
                    inject_pos = pos + 2  # one ahead injection pos
                    return True
            return False

        while inject_pos < len(polymer) - 1:
            for p in range(inject_pos, len(polymer) - 1):
                if loop(p):
                    break

    return count(polymer)


def split(polymer):
    pairs = [polymer[:2]]
    for i in range(1, len(polymer) - 1):
        pairs.append(polymer[i:i + 2])
    return pairs


def collect(pair, lookup, instructions, steps):
    if steps == 0:
        return {pair: 1}
    counter = Counter()
    if pair in instructions:
        new = instructions[pair]
        left = pair[0] + new
        right = new + pair[1]
        counter += collect(left, lookup, instructions, steps - 1)
        counter += collect(right, lookup, instructions, steps - 1)
    return counter


def find_polymers1(data, steps):
    polymer, instructions = parse_polymers(data)
    pairs = {x: 0 for x in instructions}
    counter = {x: 0 for x in instructions.values()}

    for pos in range(len(polymer) - 1):
        pairs[polymer[pos:pos+2]] += 1
    for p in polymer:
        counter[p] += 1

    # the generated never disappear so we can count them all
    for _ in range(steps):
        new_pairs = {k: 0 for k, v in pairs.items()}  # initially 0 in next loop
        for pair, pair_count in pairs.items():
            if pair_count > 0 and pair in instructions:
                val = instructions[pair]
                left = pair[0] + val
                right = val + pair[1]
                new_pairs[left] += pair_count   # pair_count eq to looping this if, thus
                new_pairs[right] += pair_count  # we can just add it
                counter[val] += pair_count      # and this many we add all together
        pairs = new_pairs
    return counter


def common_polymers0(data, steps):
    counter = find_polymers0(data, steps)
    most_common = max(counter, key=lambda x: counter[x])
    least_common = min(counter, key=lambda x: counter[x])
    print("Common polymer", counter[most_common] - counter[least_common])


def common_polymers(data, steps):
    counter = find_polymers1(data, steps)
    most_common = max(counter, key=lambda x: counter[x])
    least_common = min(counter, key=lambda x: counter[x])
    print("Common polymer", counter[most_common] - counter[least_common])

