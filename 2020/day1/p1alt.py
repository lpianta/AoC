input_string = input()

inputs_numbs = input_string.split()

for i in range(0, len(inputs_numbs)):  # changing the type of items in the list to int
    inputs_numbs[i] = int(inputs_numbs[i])

for x in inputs_numbs:
    for y in inputs_numbs:
        if x + y == 2020:
            print(x*y)
