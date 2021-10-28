# Memory: 29200KB , Time: 68ms
from sys import stdin
from itertools import combinations

while True:

    container = list(map(int, stdin.readline().split()))

    if container[0] == 0:
        break

    test_case = container[1:]
    result = combinations(test_case, 6)

    for item in result:
        print(f'{item[0]} {item[1]} {item[2]} {item[3]} {item[4]} {item[5]}')

    print()