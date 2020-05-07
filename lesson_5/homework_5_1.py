# FOR LOOPS EXERCISES

# Enter your name, save it in name variable and create function print_name_three_times which returns
# value that is equal to your name three times

name_1 = 'Inga'


def print_name_three_times(name_1):
    return name_1 * 3


# Modify your previous program so that it will enter your name (save it in variable  name_2)
# and a number
# (save in variable number) and then display their name that number of times.
# Each time add your name to result
# variable

name_2 = 'Inga'
number_1 = 6


def print_name_number_times(number_1, name_2):
    return name_2 * number_1


# Enter a random string, which includes only digits.
# Write function sum_digits which find a sum of digits in this string

string_number_1 = '123'


def sum_digits(string_number_1):
    result = 0
    for char in string_number_1:
        result = result + int(char)
    return result


print(sum_digits('123'))


# Create function which sums up all even numbers between 2 and 100 (include 100)

def sum_even_numbers():
    result = 0
    for number in range(2, 101):
        if (number % 2) == 0:
            result = result + number
    return result

print(sum_even_numbers())
