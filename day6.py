example = '''3,4,3,1,2'''


def lantern_fish_population_dummy(data, days=80):
    population = [int(x) for x in data[0].split(',')]
    for d in range(0, days):
        sz = len(population)
        for index in range(0, sz):
            if population[index] == 0:
                population.append(8)
                population[index] = 6
            else:
                population[index] -= 1
    print("Population after", days, "is", len(population))


def lantern_fish_population(data, days=80):
    population = [int(x) for x in data[0].split(',')]
    fish_states = [0] * 9  # there are fishes from 0 to 8
    for p in population:
        fish_states[p] += 1
    for d in range(days):   # how may fishes in state for a day
        first = fish_states[0]
        for i in range(1, 8 + 1):
            fish_states[i - 1] = fish_states[i]
        fish_states[6] += first  # rotated
        fish_states[8] = first   # breeded

    total = 0   # how many fishes in different states
    for f in fish_states:
        total += f
    print("Population after", days, "is", total)
