import os

text = open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt', 'r').read()
# text = open(os.path.dirname(os.path.realpath(__file__)) + '/demo.txt', 'r').read()

# convert file into array with each line being an element
textArray = text.split('\n')
# remove empty list resulting from newline
# print(textArray)
del textArray[-1]

safe = 0
for line in textArray:
    numbers = line.split()

    signOfDiff = [ ]
    n = 0
    # loop through the numbers
    for number in range(len(numbers) - 1):
        # check if numbers diff's are less than 3
        if abs(int(numbers[number]) - int(numbers[number + 1])) <= 3:
            # if true, add diff's to array so their signs are checked later
            signOfDiff.append(int(numbers[number]) - int(numbers[number + 1]))
            n = n + 1

    # check and see if that number of times the numbers incremented in less than three matched the number of numbers
    if n == int(len(numbers) - 1):
        # check if ALL numbers are increasing or decreasing
        if all(item > 0 for item in signOfDiff) or all(item < 0 for item in signOfDiff):
            safe = safe + 1

print(safe)
