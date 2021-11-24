'''
Find two entires in the input that sum to 2020
and then multiply those numbers together
'''

with open("/Users/rjc/advent-of-code-2021/test/input.txt") as f:
    values = [int(x) for x in f]
f.close()

# Values contains all number in list, run two sum on it 
nums_seen = set()

for num in values:
    difference = 2020 - num
    if difference in nums_seen:
        print("Number 1: {}, Number 2: {}, product of two: {}", num, difference, num * difference)
        break
    nums_seen.add(num)

