import itertools

example = '''--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14
'''


def permuted(v):
    p = [None] * 48
    p1 = [x[:3] for x in itertools.permutations([v[0], v[1], v[2]])]
    for i in range(6):
        p[i] = p1[i]
    for i in range(6):
        p[6 + i] = (-p1[i][0], p1[i][1], p1[i][2])
    for i in range(6):
        p[12 + i] = (p1[i][0], -p1[i][1], p1[i][2])
    for i in range(6):
        p[18 + i] = (p1[i][0], p1[i][1], -p1[i][2])
    for i in range(6):
        p[24 + i] = (-p1[i][0], -p1[i][1], p1[i][2])
    for i in range(6):
        p[30 + i] = (p1[i][0], -p1[i][1], -p1[i][2])
    for i in range(6):
        p[36 + i] = (-p1[i][0], p1[i][1], -p1[i][2])
    for i in range(6):
        p[42 + i] = (-p1[i][0], -p1[i][1], -p1[i][2])
    return p


def rotated(v, rot):
    p1 = [x[:3] for x in itertools.permutations([v[0], v[1], v[2]])]
    if 0 <= rot < 6:
        return p1[rot]
    if 6 <= rot < 12:
        return -p1[rot - 6][0], p1[rot - 6][1], p1[rot - 6][2]
    if 12 <= rot < 18:
        return p1[rot - 12][0], -p1[rot - 12][1], p1[rot - 12][2]
    if 18 <= rot < 24:
        return p1[rot - 18][0], p1[rot - 18][1], -p1[rot - 18][2]
    if 24 <= rot < 30:
        return -p1[rot - 24][0], -p1[rot - 24][1], p1[rot - 24][2]
    if 30 <= rot < 36:
        return p1[rot - 30][0], -p1[rot - 30][1], -p1[rot - 30][2]
    if 36 <= rot < 42:
        return -p1[rot - 36][0], p1[rot - 36][1], -p1[rot - 36][2]
    if 42 <= rot < 48:
        return -p1[rot - 42][0], -p1[rot - 42][1], -p1[rot - 42][2]
    return None


def parse_scanners(data):
    scanners = []
    for ln in data:
        if len(ln) == 0:
            continue
        elif ln[:3] == '---':
            scanners.append([])
        else:
            scanners[-1].append(tuple(int(x) for x in ln.split(',')))
    return scanners


def find_matches(points0, points1):
    deltas = {}
    found = None
    for p1 in points0:
        for p2 in points1:
            po = permuted(p2)
            for p in range(len(po)):
                d = (p1[0] - po[p][0], p1[1] - po[p][1], p1[2] - po[p][2])
                at = (d, p)
                if at in deltas:
                    deltas[at] += 1
                    if deltas[at] >= 12:
                        found = at
                        break
                else:
                    deltas[at] = 1
            if found:
                break
        if found:
            break
    return found


def calc_values(scanners):
    rotation_map = {}

    slen = len(scanners)
    for j in range(slen):
        for i in range(slen):
            if i != j:
                delta = find_matches(scanners[j], scanners[i])
                rotation_map[(j, i)] = delta

    max_len = len(max(scanners, key=len))

    values = set(scanners[0])
    for s in range(1, slen):
        value_list = [[None for _ in range(max_len)] for s in range(1, slen + 1)]
        value_list[s] = scanners[s]

        def loop():
            for j in range(slen):
                for i in range(slen):
                    delta = rotation_map.get((j, i))
                    if delta:
                        if value_list[i][0] and value_list[j][0] is None:
                            for k in range(len(value_list[i])):
                                if not value_list[i][k]:
                                    continue
                                r = rotated(value_list[i][k], delta[1])
                                t = (delta[0][0] + r[0], delta[0][1] + r[1], delta[0][2] + r[2])
                                value_list[j][k] = t
                            return

        while not value_list[0][0]:
            loop()

        for v in value_list[0]:
            if v:
                values.add(v)

    return values, rotation_map


def beacon_count(data):
    scanners = parse_scanners(data)
    values, _ = calc_values(scanners)
    print("Beacons:", len(values))


def manhattan_distance(data):
    scanner_data = parse_scanners(data)
    _, rot = calc_values(scanner_data)

    slen = len(scanner_data)
    scanners = [(0, 0, 0)] + [None for _ in range(slen - 1)]

    for s in range(1, slen):
        value_list = [None for s in range(1, slen + 1)]
        value_list[s] = (0, 0, 0)

        def loop():
            for j in range(slen):
                for i in range(slen):
                    at = (j, i)
                    delta = rot.get(at)
                    if delta and value_list[i] and value_list[j] is None:
                        r = rotated(value_list[i], delta[1])
                        t = (delta[0][0] + r[0], delta[0][1] + r[1], delta[0][2] + r[2])
                        value_list[j] = t
                        return

        while not value_list[0]:
            loop()

        scanners[s] = value_list[0]

    maximum = 0
    for j, p0 in enumerate(scanners):
        for i in range(j + 1, len(scanners)):
            p1 = scanners[i]
            d = (abs(p0[0] - p1[0]),
                 abs(p0[1] - p1[1]),
                 abs(p0[2] - p1[2]))
            man = d[0] + d[1] + d[2]
            if man > maximum:
                maximum = man
    print("Manhattan distance:", maximum)
