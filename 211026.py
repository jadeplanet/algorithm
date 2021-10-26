from sys import stdin

n = int(stdin.readline())
time_list = list(map(int, stdin.readline().split()))
time_list.sort()

total = 0
for i in range(n):
    for j in range(i + 1):
        total += time_list[j]

print(total)