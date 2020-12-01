import itertools

input_string = input()

inputs_numbs = input_string.split()

for i in range(0, len(inputs_numbs)):  # changing the type of items in the list to int
    inputs_numbs[i] = int(inputs_numbs[i])

for numbers in itertools.combinations(inputs_numbs, 2): # making the sum
    if sum(numbers) == 2020:
        result_index_list = [inputs_numbs.index(position) for position in numbers] # storing the 2 resulting indexes in a list
        num1 = inputs_numbs[result_index_list[0]]  # assigning the numbers to individual variable
        num2 = inputs_numbs[result_index_list[1]]
        print(num1, num2, num1 * num2) # printing the numbers and the multiplication result
