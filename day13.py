import re

example = '''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
'''


def visible_dots(data):
    dot_list = []
    folds = []
    for ln in data:
        m_c = re.match(r'(\d+)\,(\d+)', ln)
        if m_c:
            dot_list.append((int(m_c.group(1)), int(m_c.group(2))))
        m_e = re.match(r'fold\s+along\s+([a-z]+)=(\d+)', ln)
        if m_e:
            folds.append((m_e.group(1), int(m_e.group(2))))

    def add(dot):
        if dot[1] in dots:
            dots[dot[1]].add(dot[0])
        else:
            dots[dot[1]] = set([dot[0]])

    def remove(dot):
        dots[dot[1]].remove(dot[0])
        if len(dots[dot[1]]) == 0:
            dots.pop(dot[1])

    def count():
        return sum([len(s) for _, s in dots.items()])

    dots = {}
    for d in dot_list:
        add(d)

    at = 0

    # print("Dots at ", at, ":", count())

    for f, fold in folds:
        if f == 'y':
            moves = []
            for y, xs in dots.items():
                if y > fold:
                    for x in xs:
                        moves.append((x, y))
            for m in moves:
                remove(m)
                add(((m[0]), fold - m[1] + fold))
        if f == 'x':
            moves = []
            for y, xs in dots.items():
                for x in xs:
                    if x > fold:
                        moves.append((x, y))
            for m in moves:
                remove(m)
                add(((fold - m[0] + fold), m[1]))
        at += 1
        if at == 1:
            print("Dots at ", at, ":", count())

    width = max(max(dots.values(), key=max)) + 1
    height = max(dots) + 1

    for y in range(height):
        if y in dots:
            for x in range(width):
                if x in dots[y]:
                    print('#', end='')
                else:
                    print('.', end='')
        else:
            print('.' * width, end='')
        print('\n', end='')


