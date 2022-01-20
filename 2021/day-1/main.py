import sys

def part_one(input: list) -> str:
    inc_count: int = 0

    for index, depth in enumerate(input):
        last: int = input[index - 1] if index != 0 else 0
        larger: bool = last <= depth

        if larger and index != 0:
            inc_count += 1
    
    return str(inc_count)

def part_two(input: list) -> str:
    inc_count: int = 0
    last_index: int = len(input) - 1
    sum: int = 0
    previous: int = 0
    
    for index, depth in enumerate(input):
        is_sumable: bool = index + 1 < last_index and index + 2 <= last_index
        if is_sumable:
            sum = depth + input[index + 1] + input[index + 2]

            if sum > previous and index != 0:
                inc_count += 1

            previous = sum
    
    return str(inc_count)

if __name__ == '__main__':
    input: list = []
    path: str = f'{sys.path[0]}/input_test.txt' if len(sys.argv) > 1 and sys.argv[1] == 'test' else f'{sys.path[0]}/input.txt'

    with open(path, 'r') as file:
        for line in file.readlines():
            input.append(int(line.replace('\n', '')))

    print(f'Part One: {part_one(input)}')
    print(f'Part Two: {part_two(input)}')