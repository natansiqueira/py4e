"""
Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
"""
import re

print(sum([int(n) for n in re.findall('[0-9]+', open('actual_data.txt').read())]))
