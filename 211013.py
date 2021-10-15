from sys import stdin

N, M = map(int, stdin.readline().split())

target = [stdin.readline().strip() for _ in range(N)]
container = [stdin.readline().strip() for _ in range(M)]
result = [item for item in container if item in target]

print(len(result))