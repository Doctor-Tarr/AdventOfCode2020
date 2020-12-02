import os
import sys
import itertools

file = os.path.join(sys.path[0], 'passwords.list')
print(file)

def load_file(filename):
    with open(filename, 'r') as f:
        pw_list =  f.readlines()
        print("Total Passwords:         " + str(len(pw_list)))

    return pw_list


def check_password_count(pw_list):
    valid_count = 0

    for item in pw_list:
        rule = item.split(':')[0]
        pw = item.split(':')[1]

        rule_char = rule.split()[1]
        rule_min = int(rule.split()[0].split('-')[0])
        rule_max = int(rule.split()[0].split('-')[1])

        # count number of times the rule character is in the pw
        count = pw.count(rule_char)

        # see if it matches the rule
        if rule_min <= count <= rule_max:
            valid_count += 1 


    print('Valid based on count:    ' + str(valid_count))

def check_password_possition(pw_list):
    valid_count = 0


    for item in pw_list:
        rule = item.split(':')[0]
        pw = item.split(':')[1]

        rule_char = rule.split()[1]
        pos_1 = int(rule.split()[0].split('-')[0])
        pos_2 = int(rule.split()[0].split('-')[1])

        # print('Checking if ' + rule_char + ' is EITHER in position ' + str(pos_1) + ' OR ' + str(pos_2))
        # print('  in:  ' + pw)

        in_1 = rule_char == pw[pos_1]
        in_2 = rule_char == pw[pos_2]

        if in_1 != in_2:
            print('VALID')
            print(pw)
            valid_count += 1


    print('Valid based on position: ' + str(valid_count))
    return


if __name__ == '__main__':
    password_list = load_file(file)
    check_password_count(password_list)
    check_password_possition(password_list)