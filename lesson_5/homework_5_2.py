# WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1, then enter a character and
# save it in the variable char_1.
# Write function counter, which will count how many
# times your character is included in your string

string_1 = 'Spring'
char_1 = 'p'


def counter(string, char):
    return string_1.count(char_1)


# Enter a random number and save it in variable number_1.
# Then create a function number_multiplication
# that will multiply all the digits together and return the result.

number_1 = 222


def number_multiplication(number):
    index = 0
    result = 1
    while index < len(str(number)):
        result *= int(str(number)[index])
        index += 1
    return result


# Enter a random number and save it in variable number_2. Then create function number_reverse
# which will return
# a number with digits of number_1 in reverse order

number_2 = 467


def number_reverse(number):
    result = ''
    index = len(str(number_2))
    while index > 0:
        result += str(number_2)[index - 1]
        index -= 1
    return int(result)


print(number_reverse(467))
