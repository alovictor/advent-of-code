import sys

def part_one(input: list) -> str:
    return None


def part_two(input: list) -> str:
    return None


if __name__ == '__main__':
    input: list = []
    path: str = f'{sys.path[0]}/input_test.txt' if len(sys.argv) > 1 and sys.argv[1] == 'test' else f'{sys.path[0]}/input.txt'

    with open(path, 'r') as file:
        for line in file.readlines():
            input.append(line.replace('\n', ''))

    print(f'Part One: {part_one(input)}')
    print(f'Part Two: {part_two(input)}')