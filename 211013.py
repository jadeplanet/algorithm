from sys import stdin

N, M = map(int, stdin.readline().split())

target = [stdin.readline().strip() for _ in range(N)]
container = [stdin.readline().strip() for _ in range(M)]

# 주의: 고유한 값을 남기기 위해 set 함수를 사용하면 정답이 나오지 않음
result = [item for item in container if item in target]

print(len(result))