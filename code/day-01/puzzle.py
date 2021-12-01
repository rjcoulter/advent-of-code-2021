import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Gather elements in an array
with open(os.path.join(__location__, 'input.txt')) as f:
    values = [int(x) for x in f]
f.close()

# Iterate and record how many increases there are
increases = 0
for i in range(1, len(values)):
    if values[i] > values[i - 1]: increases += 1

print(increases)
