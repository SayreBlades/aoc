from collections import namedtuple
from collections import defaultdict

Coords = namedtuple('Coords', ['y', 'x'])


def get_data(fname):
    data = []
    with open(fname) as f:
        for l in f:
            x1, y1, x2, y2 = [
                int(n)
                for o in l.replace('\n', '').split('->')
                for n in o.split(',')
            ]
            data.append((Coords(y1, x1), Coords(y2, x2)))
    return data


def is_strait(c1, c2):
    return (c1.x == c2.x or c1.y == c2.y)


def step(c1, c2):
    xdiff = c2.x - c1.x
    ydiff = c2.y - c1.y
    xstep = (xdiff // abs(xdiff)) if xdiff else 0
    ystep = (ydiff // abs(ydiff)) if ydiff else 0
    return Coords(c1.y + ystep, c1.x + xstep)


def expand_line(c1, c2):
    coords = []
    while c1 != c2:
        coords.append(c1)
        c1 = step(c1, c2)
    coords.append(c2)
    return coords


def part1(fname):
    data = get_data(fname)
    ecoords = [
        c
        for c1, c2 in data if is_strait(c1, c2)
        for c in expand_line(c1, c2)
    ]
    occurrences = defaultdict(lambda: 0)
    for coords in ecoords:
        occurrences[coords] += 1
    return len([v for v in occurrences.values() if v > 1])


def part2(fname):
    data = get_data(fname)
    all_coords = [
        c
        for c1, c2 in data
        for c in expand_line(c1, c2)
    ]
    occurrences = defaultdict(lambda: 0)
    for coords in all_coords:
        occurrences[coords] += 1
    return len([v for v in occurrences.values() if v > 1])


if __name__ == '__main__':
    print(part1('input_test.txt'))  # 5
    print(part1('input.txt'))       # 7414
    print(part2('input_test.txt'))  # 12
    print(part2('input.txt'))       # 19676
