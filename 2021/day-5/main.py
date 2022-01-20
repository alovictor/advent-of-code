import sys
from pprint import pprint

def part_one(input: list) -> str:
    map: list = make_map(input)
    
    for p in range(0, len(input), 4):
        x1 = input[p]
        y1 = input[p + 1]
        x2 = input[p + 2]
        y2 = input[p + 3]

        if x1 != x2 and y1 != y2:
            continue
        
        # print(x1, y1, x2, y2)
        
        points: list = make_line(x1, y1, x2, y2)

        for point in range(0, len(points), 2):
            x = points[point]
            y = points[point + 1]
            map[y][x] += 1

    # print_map(map)

    result: int = 0

    for line in map:
        for point in line:
            if point > 1:
                result += 1
    
    return result

def make_map(input: list) -> list:
    xs = [input[x] for x in range(0, len(input), 2)]
    ys = [input[y] for y in range(1, len(input), 2)]

    width = max(xs)
    height = max(ys)
    map = []

    for y in range(height + 1):
        map.append([])
        for x in range(width + 1):
            map[y].append(0)
    
    return map


def make_line(x1: int, y1: int, x2: int, y2: int) -> list:
    points: list = []

    if x1 == x2 or y1 == y2:
        for x in range(min(x1, x2) if x1 != x2 else x1, max(x1, x2) + 1 if x1 != x2 else x1 + 1):
            for y in range(min(y1, y2) if y1 != y2 else y1, max(y1, y2) + 1 if y1 != y2 else y1 + 1):
                if x1 == x2:
                    points.append(x1)
                else:
                    points.append(x)

                if y1 == y2:
                    points.append(y1)
                else:
                    points.append(y)
    else:
        xs: list = [x for x in range(min(x1, x2), max(x1, x2) + 1)]
        ys: list = [y for y in range(min(y1, y2), max(y1, y2) + 1)]

        if x1 > x2:
            xs.reverse()
        if y1 > y2:
            ys.reverse()
        # print(xs, ys)
        
        for i in range(len(xs)):
            points.append(xs[i])
            points.append(ys[i])

    return points

def part_two(input: list) -> str:
    map: list = make_map(input)
    
    for p in range(0, len(input), 4):
        x1 = input[p]
        y1 = input[p + 1]
        x2 = input[p + 2]
        y2 = input[p + 3]
        
        # print(x1, y1, x2, y2)
        
        points: list = make_line(x1, y1, x2, y2)

        for point in range(0, len(points), 2):
            x = points[point]
            y = points[point + 1]
            map[y][x] += 1

    # print_map(map)

    result: int = 0

    for line in map:
        for point in line:
            if point > 1:
                result += 1
    
    return result

def print_map(map:list) -> None:
    for line in map:
        for cell in line:
            if cell > 0:
                print(f'\033[92m{cell}\033[0m', end= ' ')
            else:
                print(cell, end=' ')
        print('')

if __name__ == '__main__':
    input: list = []
    path: str = f'{sys.path[0]}/input_test.txt' if len(sys.argv) > 1 and sys.argv[1] == 'test' else f'{sys.path[0]}/input.txt'

    with open(path, 'r') as file:
        for line in file.readlines():
            line = line.replace('\n', '').replace(' -> ', ' ').replace(',', ' ')
            for n in line.split():
                input.append(int(n))

    print(f'Part One: {part_one(input)}')
    print(f'Part Two: {part_two(input)}')