import day1
import day2
'''
import day3
import day4
import day5
import day6
import day7
import day8
import day9
import day10
import day11
import day12
import day13
import day14
import day15
import day16
import day17
import day18
import day19
import day20
import day21
import day22
import day23
import day24
import day25
'''

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


