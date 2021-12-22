import day1
import day2
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

import time


def read_example(str):
    return str.splitlines()


def read_input(fn):
    lines = []
    with open(fn) as f:
        for l in f:
            lines.append(l.rstrip())
    return lines


def do_example(day, call):
    day.call(read_example(day.example))


def do_solution(day, call):
    day.call(read_input('data.input'))


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
    

    day8.count_easy_digits(read_example(day8.example))
    day8.count_easy_digits(read_input('data/input8.txt'))

    day8.digit_output(read_example(day8.example))
    day8.digit_output(read_input('data/input8.txt'))
    
    day9.risk_level_sum(read_example(day9.example))
    day9.risk_level_sum(read_input('data/input9.txt'))

    day9.basin_top_mul(read_example(day9.example))
    day9.basin_top_mul(read_input('data/input9.txt'))
    
    day10.corrupt_score(read_example(day10.example))
    day10.corrupt_score(read_input('data/input10.txt'))

    day10.autocomplete_score(read_example(day10.example))
    day10.autocomplete_score(read_input('data/input10.txt'))
    

    day11.octopus_flash_count(read_example(day11.example))
    day11.octopus_flash_count(read_input('data/input11.txt'))

    day11.octopus_all_flash(read_example(day11.example))
    day11.octopus_all_flash(read_input('data/input11.txt'))
    

    day12.count_paths(read_example(day12.example))
    day12.count_paths(read_input('data/input12.txt'))

    day12.count_paths2(read_example(day12.example))
    day12.count_paths2(read_input('data/input12.txt'))

    
    day13.visible_dots(read_example(day13.example))
    day13.visible_dots(read_input('data/input13.txt'))
    
    
    day14.common_polymers(read_example(day14.example), 10)
    day14.common_polymers(read_input('data/input14.txt'), 10)
    day14.common_polymers(read_input('data/input14.txt'), 40)
    
    

    day15.find_path(read_example(day15.example))
    day15.find_path(read_input('data/input15.txt'))
    day15.find_path_extended(read_example(day15.example))
    day15.find_path_extended(read_input('data/input15.txt'))
    
    # day16.parse_transmissions(read_example(day16.example0))
    day16.parse_transmissions(read_input('data/input16.txt'))

    # day16.calc_transmissions(read_example(day16.example1))

    day16.calc_transmissions(read_input('data/input16.txt'))
    
    day17.trajectory_high(day17.example)
    day17.trajectory_high(day17.input_1)

    day17.count_trajectory(day17.example)
    day17.count_trajectory(day17.input_1)
    
    day18.snail_fish_magnitude(read_example(day18.example))
    day18.snail_fish_magnitude(read_input('data/input18.txt'))

    day18.largest_snail_fish_magnitude(read_example(day18.example))
    day18.largest_snail_fish_magnitude(read_input('data/input18.txt'))
    

    day19.beacon_count(read_example(day19.example))
    day19.beacon_count(read_input('data/input19.txt'))

    day19.manhattan_distance(read_example(day19.example))
    day19.manhattan_distance(read_input('data/input19.txt'))
    

    day20.count_lit_pixels(read_example(day20.example), 2)
    day20.count_lit_pixels(read_input('data/input20.txt'), 2)

    day20.count_lit_pixels(read_example(day20.example), 50)
    day20.count_lit_pixels(read_input('data/input20.txt'), 50)
    
    
    day21.dirac_dice_practice(4, 8)
    day21.dirac_dice_practice(6, 7)

    day21.dirac_dice(4, 8)
    day21.dirac_dice(6, 7)
    '''

    day22.cubes_on100x100x100(read_example(day22.example))
    day22.cubes_on100x100x100(read_input('data/input22.txt'))

    day22.cubes_on100x100x100(read_example(day22.example))
    day22.cubes_on_all(read_example(day22.example_part2))
    day22.cubes_on_all(read_input('data/input22.txt'))
