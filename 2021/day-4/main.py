import sys
from pprint import pprint

def part_one(input: dict) -> str:
    winner, current = check_winner(input['numbers'], input['tables'])

    sum: int = 0

    for line in winner['table']:
        for number in line:
            if number['checked'] == False:
                sum += number['number']
    
    return sum * current

def part_two(input: dict) -> str:
    winners: list = check_all_winners(input['numbers'], input['tables'])

    winner: dict = winners[-1]['winner']
    current: int = winners[-1]['current']

    sum: int = 0

    for line in winner['table']:
        for number in line:
            if number['checked'] == False:
                sum += number['number']
    
    return sum * current

def check_winner(numbers: list, tables: list) -> tuple:

    for current in numbers:
        for table in tables:
            for line in table['table']:
                for number in line:
                    if number['number'] == current:
                        number['checked'] = True
                
            table['bingo'] = check_bingo(table)

            if table['bingo']:
                return table, current

def check_all_winners(numbers: list, tables: list) -> list:
    winners: list = []
    has_winner: bool = False
    winners_index: list = []

    for current in numbers:
        for index, table in enumerate(tables):
            for line in table['table']:
                for number in line:
                    if number['number'] == current:
                        number['checked'] = True
                
            table['bingo'] = check_bingo(table)

            if table['bingo']:
                winners.append({
                    'winner': table,
                    'current' : current
                })
                has_winner = True
                winners_index.append(index)
        
        if has_winner and len(winners_index) > 0:
            winners_index.reverse()
            for index in winners_index:
                tables.pop(index)
            winners_index.clear()

    
    return winners


def check_bingo(table: dict) -> bool:

    for x in range(5):
        count_checked: int = 0
        for y in range(5):
            if table['table'][y][x]['checked'] == True:
                count_checked += 1
        
        if count_checked == 5:
            return True

    for line in table['table']:
        count_checked: int = 0

        for number in line:
            if number['checked'] == True:
                count_checked += 1

        if count_checked == 5:
            return True    

    return False

def get_dicts(path: str) -> dict:
    input: dict = {
        'numbers' : [],
        'tables' : []
    }

    with open(path, 'r') as file:
        input['numbers'] = [int(x) for x in file.readline().replace('\n', '').split(',')]
        count_lines: int = 0
        for line in file.readlines():
            line = line.replace('\n', '')
            if line == '':
                count_lines = 0
                input['tables'].append({
                    'table' : [],
                    'bingo' : False
                })
                continue
            if count_lines < 5:
                input['tables'][-1]['table'].append([])
                for number in line.strip().split():
                    input['tables'][-1]['table'][-1].append({
                        'number' : int(number),
                        'checked' : False
                    })
    return input

def print_table(table: dict) -> None:
    print(f"\nWinner: {table['bingo']}")
    for line in table['table']:
        for number in line:
            n = str(number['number'])
            if len(n) < 2:
                n = ' ' + n
            if number['checked']:
                print(' \033[92m' + n + '\033[0m ', end='')
            else:
                print(f' {n} ', end='')
        print('')
    print('\n')

if __name__ == '__main__':
    path: str = f'{sys.path[0]}/input_test.txt' if len(sys.argv) > 1 and sys.argv[1] == 'test' else f'{sys.path[0]}/input.txt'

    print(f'Part One: {part_one(get_dicts(path))}')
    print(f'Part Two: {part_two(get_dicts(path))}')