import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Gather elements in an array
with open(os.path.join(__location__, 'input.txt')) as f:
    values = [int(x) for x in f]
f.close()

increases = 0
for i in range(len(values) - 3):
    # Get values needed for sums 
    first, second, third, fourth = values[i], values[i + 1], values[i + 2], values[i + 3]
    first_sum = first + second + third
    second_sum = second + third + fourth  

    if second_sum > first_sum:
        increases += 1

print(increases)