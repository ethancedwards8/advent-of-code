import os

# open file
text = open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt', 'r').read()

# make input one big array
textArray = text.split()

column1 = []
column2 = []

n = 0
# sort left column into array1 and vice versa
for number in textArray:
    if n % 2 == 0:
        column1.append(textArray[n])
    else:
        column2.append(textArray[n])

    n = n + 1

# sort from least to greatest
column1.sort()
column2.sort()

columnDiff = []

# find the difference between each
n = 0
for number in column1:
    columnDiff.append(abs(int(column2[n]) - int(column1[n])))
    n = n + 1

# print the sum
print('Part 1: ' + str(sum(columnDiff)))

# PART 2
columnSimilar = [ ]
n = 0
for number in column1:
    columnSimilar.append(int(column1[n]) * int(column2.count(column1[n])))

    n = n + 1

print('Part 2: ' + str(sum(columnSimilar)))
