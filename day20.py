
example = '''..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
'''


def parse_input(data):
    algorithm = []
    image = []
    on_image = False
    for ln in data:
        if len(ln) == 0:
            on_image = True
            continue
        if on_image:
            image.append([1 if x == '#' else 0 for x in list(ln)])
        else:
            algorithm.extend([1 if x == '#' else 0 for x in list(ln)])
    return image, algorithm


def pixel_size(image):
    return len(image[0]), len(image)


def show_image(image):
    sx, sy = image_extents(image)
    for r in range(sy[0], sy[1] + 1):
        for c in range(sx[0], sy[1] + 1):
            at = (r, c)
            if at in image:
                print('#', end='')
            else:
                print('.', end='')
        print("")


def convolute(image, background, algorithm):
    if background:
        new_background = True if algorithm[511] else False
    else:
        new_background = True if algorithm[0] else False

    new_image = {}
    sx, sy = image_extents(image)

    def is_in(rr, cc):
        return sy[0] <= rr <= sy[1] and sx[0] <= cc <= sx[1]

    for r in range(sy[0] - 1, sy[1] + 2):
        for c in range(sx[0] - 1, sy[1] + 2):
            convolution = ((r - 1, c - 1) in image if is_in(r - 1, c - 1) else background,
                           (r - 1, c) in image if is_in(r - 1, c) else background,
                           (r - 1, c + 1) in image if is_in(r - 1, c + 1) else background,

                           (r, c - 1) in image if is_in(r, c - 1) else background,
                           (r, c) in image if is_in(r, c) else background,
                           (r, c + 1) in image if is_in(r, c + 1) else background,

                           (r + 1, c - 1) in image if is_in(r + 1, c - 1) else background,
                           (r + 1, c) in image if is_in(r + 1, c) else background,
                           (r + 1, c + 1) in image if is_in(r + 1, c + 1) else background
                           )
            bin_value = ''.join(['1' if x else '0' for x in convolution])
            index = int(bin_value, 2)
            is_on = algorithm[index]
            if is_on:
                new_image[(r, c)] = 1
    return new_image, new_background


def make_image(pixels):
    width, height = pixel_size(pixels)
    image = {}
    for r in range(height):
        for c in range(width):
            if pixels[r][c]:
                image[(r, c)] = 1
    return image


def image_extents(image):
    minx = 0xFFFFFFFF
    maxx = -0xFFFFFFFF
    miny = 0xFFFFFFFF
    maxy = -0xFFFFFFFF
    for r, c in image:
        if r < miny:
            miny = r
        if r > maxy:
            maxy = r
        if c < minx:
            minx = c
        if c > maxx:
            maxx = c
    return (minx, maxx), (miny, maxy)


def count_lit_pixels(data, steps):
    pixels, algo = parse_input(data)
    image = make_image(pixels)
    background = 0

    for _ in range(steps):
        image, background = convolute(image, background, algo)

    sx, sy = image_extents(image)
    on = 0
    for r in range(sy[0], sy[1] + 1):
        for c in range(sx[0], sy[1] + 1):
            at = (r, c)
            if at in image:
                on += 1

    print("Pix on", on)



