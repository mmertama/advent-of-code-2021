import day1
import day2
import day3
import day4
import day5
import day6
import day7
import day8

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
    '''
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
    
    day5.line_overlap_orthogonal(read_example(day5.example))
    day5.line_overlap_orthogonal(read_input('data/input5.txt'))

    day5.line_overlap_all(read_example(day5.example))
    day5.line_overlap_all(read_input('data/input5.txt'))

    day6.lantern_fish_population(read_example(day6.example), 80)
    day6.lantern_fish_population(read_input('data/input6.txt'), 80)
    day6.lantern_fish_population(read_example(day6.example), 256)
    day6.lantern_fish_population(read_input('data/input6.txt'), 256)
    
    day7.align_submarines(read_example(day7.example))
    day7.align_submarines(read_input('data/input7.txt'))

    day7.align_submarines_x2(read_example(day7.example))
    day7.align_submarines_x2(read_input('data/input7.txt'))
    '''

    day8.count_easy_digits(read_example(day8.example))
    day8.count_easy_digits(read_input('data/input8.txt'))

    day8.digit_output(read_example(day8.example))
    day8.digit_output(read_input('data/input8.txt'))