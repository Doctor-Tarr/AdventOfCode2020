import os
import sys
import itertools

file = os.path.join(sys.path[0], 'expenses.list')
print(file)

def process_expenses(filename, count):
    
    with open(filename, 'r') as f:

        expense_ints = [int(i) for i in f.readlines()]

        combo_tuple = [combo for combo in itertools.combinations(expense_ints, count) if sum(combo) == 2020]
        combo = (combo_tuple[0])
        print(' The ' + str(count) + ' expenses that add up to 2020 are: ')
        print(*combo)

        result = 1
        for i in combo:
            result = result * i

        print('The product of those numbers is: ' + str(result))

if __name__ == '__main__':
    process_expenses(file, 2)
    process_expenses(file, 3)
