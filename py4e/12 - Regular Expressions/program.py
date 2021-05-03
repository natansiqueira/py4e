"""
Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
"""
import re

file_name = input("Enter file name: ")
try:
    file_handle = open(file_name)
except:
    print('File cannot be opened:', file_name)
    exit()

result = 0
for line in file_handle:
    numbers = re.findall('[0-9]+', line)
    if len(numbers) > 0:
        result = result + sum([int(n) for n in numbers])

print(result)