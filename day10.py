
example = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]'''


def corrupt_score(data):
    opens = '<[({'
    closes = '>])}'
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0
    for ln in data:
        stack = []
        for c in ln:
            if c in opens:
                stack.append(c)
            else:
                p = stack.pop()
                ic = closes.find(c)
                io = opens.find(p)
                if ic != io:
                    score += points[c]
                    break
    print("Corrupt score:", score)


def autocomplete_score(data):
    opens = '<[({'
    closes = '>])}'
    points = {'(': 1, '[': 2, '{': 3, '<': 4}
    scores = []
    for ln in data:
        stack = []
        for c in ln:
            if c in opens:
                stack.append(c)
            else:
                p = stack.pop()
                ic = closes.find(c)
                io = opens.find(p)
                if ic != io:
                    stack = []
                    break
        if len(stack) > 0:
            score = 0
            for c in reversed(stack):
                score *= 5
                score += points[c]
            scores.append(score)
    scores.sort()
    print("score", scores[int(len(scores) / 2)])






