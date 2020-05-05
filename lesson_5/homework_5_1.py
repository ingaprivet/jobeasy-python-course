# Homework 5.1
# FOR LOOPS EXERCISES

# Enter your name, save it in name variable and then display their name three times.
# Each time add your name to result
# variable

name1 = 'Inga'
for i in range(3):
    result_1 = name1

# Modify your previous program so that it will enter your name (save it in variable  name_2) and a number
# (save in variable number) and then display their name that number of times. Each time add your name to result
# variable

name_2 = 'Inga'
number = 6

for i in range(number):
    result_2 = name_2
    print(result_2)

# Enter your name, save in name_3 variable and display each letter in your name on a separate line. Each time increase
# variable counter_1 by 1. After your code will finished, assign result_3 variable as a counter with counted value

name_3 = 'Inga'
counter_1 = 0

for i in range(len(name_3)):
    result_3 = name_3[counter_1]
    counter_1 += 1
    print(result_3)
result_3 = counter_1

# Enter a random number below 50, save it in number_2 variable and then count down from 50 to that number, making sure
# you show the number they entered in the output. Each time decrease variable counter_2 by 1. After your code will
# finished, assign result_3 variable as a counter with counted value

number_2 = 40
counter_2 = 50

for i in range(counter_2 - number_2):
    counter_2 -= 1
    print(counter_2)
result_4 = counter_2

