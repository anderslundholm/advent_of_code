def check_double_digit(number):
    return len(str(number)) != len(set(str(number)))


def check_double_digit2(i):
    return len(str(i)) != len(set(str(i)))


def calc_possible_passwords():
    count = 0
    for number in range(356261, 846303):
        if not check_double_digit(number):
            continue
        number_string = (str(number))
        adjacent = False
        for index, digit in enumerate(number_string):
            if index != 0:
                if int(digit) < int(number_string[index-1]):
                    break
                if (int(digit) == int(number_string[index-1]) and
                   number_string.count(digit) == 2):
                    print(number, index, digit)
                    adjacent = True
                if adjacent and len(number_string) == index+1:
                    count += 1
    print(count)


if __name__ == '__main__':
    # Between 356261-846303
    calc_possible_passwords()
