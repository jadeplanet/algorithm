# itertools 모듈에서 조합 함수 가져오기
from itertools import combinations

def solution(numbers):
    # 주어진 숫자 리스트 중 2개를 뽑아서 만들 수 있는 모든 조합 찾기
    container = list(combinations(numbers, 2))

    # 찾아낸 조합의 요소(a,b)들을 각각 더한 값(a+b)을 새로운 리스트에 담기
    answer = []
    for i in range(len(container)):
        sum = container[i][0] + container[i][1]
        answer.append(sum)

    # answer 리스트에서 집합(set)으로 변환하여 중복을 제거
    # 다시 리스트 형식로 변환
    # 오름차순으로 정렬한 값을 반환
    return sorted(list(set(answer)))