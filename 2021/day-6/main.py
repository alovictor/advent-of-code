import collections
import sys
from collections import Counter

def part_one(input: list) -> str:
    state: list = input.copy()

    for day in range(80):
        # print(f'Day {day if len(str(day)) > 1 else f" {day}"}: {state}')
        for index, fish in enumerate(state):
            if fish == 0:
                state.append(9)
                state[index] = 6
            else:
                state[index] -=1

    return len(state)


def part_two(input: list) -> str:
    state: collections.Counter = Counter(input)

    for day in range(256):
        # print(f'Day {day + 1}: {state}')
        borns = Counter({6 : state[0], 8 : state[0]})
        borns.update({k - 1: v for k, v in state.items() if k > 0})
        state = borns
            
    return state.total()


if __name__ == '__main__':
    input: list = []
    path: str = f'{sys.path[0]}/input_test.txt' if len(sys.argv) > 1 and sys.argv[1] == 'test' else f'{sys.path[0]}/input.txt'

    with open(path, 'r') as file:
        for line in file.readlines():
            line = line.replace('\n', '')
            for number in line.split(','):
                input.append(int(number))

    print(f'Part One: {part_one(input)}')
    print(f'Part Two: {part_two(input)}')
    