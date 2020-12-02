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
        # print(item)
        rule = item.split(':')[0]
        pw = item.split(':')[1]
        # print(rule)
        # print(pw)

        rule_char = rule.split()[1]
        rule_min = int(rule.split()[0].split('-')[0])
        rule_max = int(rule.split()[0].split('-')[1])

        # print(rule_char)
        # print("  min: " + str(rule_min))
        # print("  max: " + str(rule_max))

        # count number of times the rule character is in the pw
        count = pw.count(rule_char)
        # print("\n" + str(count) + '  ' + rule_char + ' in '+ pw)

        # see if it matches the rule
        if rule_min <= count <= rule_max:
            # print('  ' + str(count) + " IS between " + str(rule_min) + " and " + str(rule_max))
            valid_count += 1 


    print('Valid based on count:    ' + str(valid_count))

def check_password_possition(pw_list):
    valid_count = 0

    print('Valid based on position: ' + str(valid_count))
    return


if __name__ == '__main__':
    password_list = load_file(file)
    check_password_count(password_list)
    check_password_possition(password_list)