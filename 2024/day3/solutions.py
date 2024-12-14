import os
import re

# open file
text = open(os.path.dirname(os.path.realpath(__file__)) + '/input.txt', 'r').read()
# text = open(os.path.dirname(os.path.realpath(__file__)) + '/demo.txt', 'r').read()

# find all instances of mul(number,number)
multiplication = re.findall(r'mul\(\d+,\d+\)', text)

result = [ ]

for nums in multiplication:
    # find both numbers in mul(number,number)
    nums = re.findall(r'\d+', nums)

    # make a list of all the multiplied numbers
    result.append(int(nums[0]) * int(nums[1]))

print(sum(result))
