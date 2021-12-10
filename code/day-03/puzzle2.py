from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded
import os 

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def find_generic(lines, n, inverted=False):
    for x in range(n):        
        mostlyzeroes = sum(line[x] == '0' for line in lines) * 2 > len(lines)
        xored = inverted^mostlyzeroes
        lines = lines if len(lines) == 1 else [line for line in lines if (line[x] == '1')^xored]

    return int(lines[0], 2)


def find_oxygen(lines, n):    
    return find_generic(lines, n)


def find_co2(lines, n):
    return find_generic(lines, n, True)


def solve(lines):
    n = len(lines[0])
    oxygen = find_oxygen(lines, n)
    co2 = find_co2(lines, n)

    print(oxygen * co2)
    return oxygen*co2


def main():
    lines = []
    with open(os.path.join(__location__, 'input.txt')) as f:
        for line in f.readlines():
            lines.append(line.rstrip())
    print(solve(lines)) 
    return solve(lines)

main()