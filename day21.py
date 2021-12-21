example = '''Player 1 starting position: 4
Player 2 starting position: 8'''

input_data = '''Player 1 starting position: 6
Player 2 starting position: 7'''


def practice_dice(dice):
    dice += 1
    return 1 if dice > 100 else dice


def play_turn(score, start, dice):
    dice = practice_dice(dice)
    forward = dice
    dice = practice_dice(dice)
    forward += dice
    dice = practice_dice(dice)
    forward += dice
    pos = ((start + forward - 1) % 10) + 1
    score += pos
    return score, pos, dice


def dirac_dice_practice(start1, start2):
    dice = 0
    score1 = 0
    score2 = 0
    rolls = 0

    def show_loser(s):
        print("Loser score:", s * rolls)

    while True:
        rolls += 3
        score1, start1, dice = play_turn(score1, start1, dice)
        if score1 >= 1000:
            show_loser(score2)
            break
        rolls += 3
        score2, start2, dice = play_turn(score2, start2, dice)
        if score1 >= 1000:
            show_loser(score1)
            break


def move_list(start):
    moves = []
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                v = ((start + (i + j + k) - 1) % 10) + 1
                moves.append(v)
    return moves


def dirac_dice(start1, start2):

    cache = {}

    move_map = [move_list(r) for r in range(1, 10 + 1)]

    def play(pl1, pl2):

        at = (pl1, pl2)
        if at in cache:
            return cache[at]

        next_pos = move_map[pl1[0]]

        wins = 0, 0

        for p in next_pos:
            score = p + pl1[1]
            if score >= 21:
                if pl1[2] == 1:
                    wins = (wins[0] + 1, wins[1])
                else:
                    wins = (wins[0], wins[1] + 1)
                continue
            win0 = play(pl2, (p - 1, score, pl1[2]))
            wins = (wins[0] + win0[0], wins[1] + win0[1])

        at = (pl1, pl2)
        cache[at] = wins

        return wins
        
    w = play((start1 - 1, 0, 1), (start2 - 1, 0, 2))

    print("Winner is", "player1 " if w[0] > w[1] else "player2", "with", w[0] if w[0] > w[1] else w[1], "universes!")
