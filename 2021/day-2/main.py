import sys

def part_one(input: list) -> str:
    hor_pos: int = 0
    depth: int = 0

    for i in input:
        com: str = i[0]
        value: int = i[1]

        if com == 'forward':
            hor_pos += value
        elif com == 'down':
            depth += value
        else:
            depth -= value

    return str(hor_pos * depth)


def part_two(input: list) -> str:
    hor_pos: int = 0
    depth: int = 0
    aim: int = 0

    for i in input:
        com: str = i[0]
        value: int = i[1]

        if com == 'forward':
            hor_pos += value
            depth += aim * value
        elif com == 'down':
            aim += value
        else:
            aim -= value
    
    return str(hor_pos * depth)


if __name__ == '__main__':
    input: list = []
    path: str = f'{sys.path[0]}/input_test.txt' if len(sys.argv) > 1 and sys.argv[1] == 'test' else f'{sys.path[0]}/input.txt'

    with open(path, 'r') as file:
        for line in file.readlines():
            line: str = line.replace('\n', '').split()
            com: str = line[0].strip()
            value: int = int(line[1])
            input.append([com, value])

    print(f'Part One: {part_one(input)}')
    print(f'Part Two: {part_two(input)}')