import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

horizontal, depth, aim = 0, 0, 0

lines = []
with open(os.path.join(__location__, 'input.txt')) as fp:
    lines = fp.readlines()

fp.close()

for line in lines:
    dir, val = line.strip('\n').split()
    if dir == 'up':
        aim -= int(val)
    elif dir == 'down':
        aim += int(val)
    elif dir == 'forward':
        horizontal += int(val)
        depth += (aim * int(val))

print(horizontal * depth)


