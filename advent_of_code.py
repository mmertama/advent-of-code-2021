import day1
import day2
import day3
import day4

import time


def read_example(str):
    return str.splitlines()


def read_input(fn):
    lines = []
    with open(fn) as f:
        for l in f:
            lines.append(l.rstrip())
    return lines


if __name__ == "__main__":
    print("day 1", flush=True)
    day1.count_ascent(read_example(day1.example))
    day1.count_ascent(read_input('data/input1.txt'))
    day1.count_ascent_sliding_window(read_example(day1.example))
    day1.count_ascent_sliding_window(read_input('data/input1.txt'))

    day2.navigate(read_example(day2.example))
    day2.navigate(read_input('data/input2.txt'))

    day2.navigate_aim(read_example(day2.example))
    day2.navigate_aim(read_input('data/input2.txt'))

    day3.power_consumption(read_example(day3.example))
    day3.power_consumption(read_input('data/input3.txt'))

    day3.life_support(read_example(day3.example))
    day3.life_support(read_input('data/input3.txt'))

    day4.play_bingo(read_example(day4.example))
    day4.play_bingo(read_input('data/input4.txt'))

    day4.play_last_bingo(read_example(day4.example))
    day4.play_last_bingo(read_input('data/input4.txt'))



