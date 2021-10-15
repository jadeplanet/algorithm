from sys import stdin

# 첫 번째 줄 숫자 받아오기
# strip: 입력받은 문자열 오른쪽에 남아있는 '\n'을 제거.(rstrip()으로도 가능)
# int: 데이터타입을 문자열에서 숫자로 변환
num = int(stdin.readline().strip())

# 출입 기록 로그를 담을 딕셔너리 생성
# 딕셔너리의 key값은 고유한 값이기 때문에, 중복되는 key값을 입력하면 마지막으로 입력된 value만 남는다는 특징을 활용
# 즉, 예제에서 퇴근한 사람의 'enter'기록은 딕셔너리 요소에서 사라짐
# 예제의 경우, {'Baha': 'leave', 'Askar': 'enter', 'Artem': 'enter'}의 형태로 남음
# 딕셔너리의 value값이 'enter'로 남아있는 key값을 구하면 정답을 찾을 수 있음
obj = {}
for item in range(num):
  key, value = stdin.readline().strip().split()
  obj[key] = value

# key값이 'enter'인 요소를 찾아서 result 리스트에 담기
# 출근기록은 있는데 퇴근기록이 없는 사람을 찾아내는 방식
result = []
for key in obj.keys():
  if obj.get(key) == 'enter':
    result.append(key)

# '현재 회사에 있는 사람의 이름을 사전의 역순으로 출력한다.'라는 문제의 조건이 있음
# result 리스트의 요소들을 알파벳 역순으로 정렬
answer = sorted(result, reverse=True)

# 결과물 출력
for elem in answer:
  print(elem)