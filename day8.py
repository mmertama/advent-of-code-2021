
example = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce'''


def parse_digits(data):
    signals = []
    for ln in data:
        sep = ln.find('|')
        signals.append((ln[:sep].split(), ln[sep + 1:].split()))
    return signals


def count_easy_digits(data):
    signals = parse_digits(data)
    counts = {x: 0 for x in range(0, 8)}
    for s in signals:
        output = s[1]
        for o in output:
            counts[len(o)] += 1

    segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]  # 0 1 2 3 4 5 6 7 8 9
    print("easy digits", counts[segments[1]] + counts[segments[4]] + counts[segments[7]] + counts[segments[8]])


def digit_output(data):
    values = parse_digits(data)
    total = 0
    for v in values:
        digits = [None for _ in range(10)]
        digits[8] = set(list('abcdef'))
        signals = v[0]

        for s in signals:
            sig_set = set(list(s))
            if len(s) == 2:
                digits[1] = sig_set
            if len(s) == 3:
                digits[7] = sig_set
            if len(s) == 4:
                digits[4] = sig_set
            if len(s) == 7:
                digits[8] = sig_set

        while not all(digits):
            for s in signals:
                sig_set = set(list(s))
                if len(s) == 6:
                    if digits[1] and not sig_set.issuperset(digits[1]):
                        digits[6] = sig_set
                    if digits[7] and not sig_set.issuperset(digits[7]):
                        digits[6] = sig_set
                    if digits[4] and sig_set.issuperset(digits[4]):
                        digits[9] = sig_set

                if len(s) == 5:
                    if digits[1] and sig_set.issuperset(digits[1]):
                        digits[3] = sig_set
                    if digits[7] and sig_set.issuperset(digits[7]):
                        digits[3] = sig_set
                    if digits[6] and sig_set.issubset(digits[6]):
                        digits[5] = sig_set
                    if digits[9] and not sig_set.issubset(digits[9]):
                        digits[2] = sig_set

                if len(s) == 6:
                    if digits[0] and sig_set != digits[0] and digits[6] and sig_set != digits[6]:
                        digits[9] = sig_set
                    if digits[9] and sig_set != digits[9] and digits[6] and sig_set != digits[6]:
                        digits[0] = sig_set
                    if digits[0] and sig_set != digits[0] and digits[9] and sig_set != digits[9]:
                        digits[6] = sig_set
                if len(s) == 5:
                    if digits[2] and sig_set != digits[2] and digits[3] and sig_set != digits[3]:
                        digits[5] = sig_set
                    if digits[5] and sig_set != digits[5] and digits[3] and sig_set != digits[3]:
                        digits[2] = sig_set
                    if digits[2] and sig_set != digits[2] and digits[5] and sig_set != digits[5]:
                        digits[3] = sig_set
        '''
        segments = [None for _ in range(8)]
        segments[5] = digits[2].intersection(digits[1])
        segments[4] = digits[8] - digits[9]
        segments[3] = digits[8] - digits[0]
        segments[2] = digits[8] - digits[6]
        segments[1] = digits[3] - digits[5]
        segments[6] = digits[1] - segments[2]
        segments[7] = digits[3] - digits[7] - segments[3]
        segments[0] = digits[7] - segments[2] - segments[6]
        '''
        value = 0
        p = 1
        outputs = v[1]
        for o in reversed(outputs):
            out_set = set(list(o))
            for d in range(len(digits)):
                if out_set == digits[d]:
                    value += d * p
                    p *= 10

        total += value
        # print(segments)
        # print(value)

    print("sum of digits is", total)

