import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def puzzle_one():
    lines, bin_num = [], [0 for _ in range(12)]

    with open(os.path.join(__location__, 'input.txt')) as fp:
        lines = fp.readlines()

    # 12 bit numbers
    for line in lines:
        line = line.strip('\n')
        for i, n in enumerate(line):
            n = int(n)
            if n == 1:
                bin_num[i] += 1
            else:
                bin_num[i] -= 1
    res = ""
    for digit in bin_num:
        if digit < 0:
            res += "0"
        else:
            res += "1"

    gamma = int(res, 2)
    res = res.replace('1', '2')
    res = res.replace('0', '1')
    res = res.replace('2', '0')
    epsilon = int(res, 2)
    print(gamma * epsilon)

    fp.close()


puzzle_one()