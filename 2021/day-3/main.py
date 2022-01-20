import sys

def part_one(input: list) -> str:
    gamma: str = ge_rates(input)[0]
    epsilon: str = ge_rates(input)[1]
    
    gamma_int: int = int(gamma, 2)
    epsilon_int: int = int(epsilon, 2)

    return str(gamma_int * epsilon_int)



def ge_rates(input: list) -> str:
    gamma: str = ''
    epsilon: str = ''

    for i in range(len(input[0])):
        zeros: int = 0
        ones: int = 0

        for b in input:
            if b[i] == '0':
                zeros += 1
            elif b[i] == '1':
                ones += 1

        gamma += '0' if zeros > ones else '1'
        epsilon += '0' if zeros < ones else '1'

    return gamma, epsilon
    

def part_two(input: list) -> str:
    oxygen: str = oxygen_rate(input)
    carbon: str = carbon_rate(input)

    oxygen_int: int = int(oxygen, 2)
    carbon_int: int = int(carbon, 2)

    return str(oxygen_int * carbon_int)



def oxygen_rate(input: list) -> str:
    rate: str = ''
    new_input: list = input

    for i in range(len(new_input[0])):
        new_list: list = []
        zeros: int = 0
        ones: int = 0

        for b in new_input:
            if b[i] == '0':
                zeros += 1
            elif b[i] == '1':
                ones += 1
        
        for b in new_input:
            if b[i] == '0':
                if zeros > ones:
                    new_list.append(b)
            elif b[i] == '1':
                if ones >= zeros:
                    new_list.append(b)

        new_input = new_list

        if len(new_input) == 1:
            rate = new_input[0]

    return rate


def carbon_rate(input: list) -> str:
    rate: str = ''
    new_input: list = input

    for i in range(len(new_input[0])):
        new_list: list = []
        zeros: int = 0
        ones: int = 0

        for b in new_input:
            if b[i] == '0':
                zeros += 1
            elif b[i] == '1':
                ones += 1
        
        for b in new_input:
            if b[i] == '0':
                if zeros <= ones:
                    new_list.append(b)
            elif b[i] == '1':
                if ones < zeros:
                    new_list.append(b)

        new_input = new_list

        if len(new_input) == 1:
            rate = new_input[0]

    return rate


if __name__ == '__main__':
    input: list = []
    path: str = f'{sys.path[0]}/input_test.txt' if len(sys.argv) > 1 and sys.argv[1] == 'test' else f'{sys.path[0]}/input.txt'


    with open(path, 'r') as file:
        for line in file.readlines():
            input.append(line.replace('\n', ''))

    print(f'Part One: {part_one(input)}')
    print(f'Part Two: {part_two(input)}')