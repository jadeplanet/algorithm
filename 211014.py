import sys

# 람다 함수를 통한 문자열 읽기
readText = lambda: sys.stdin.readline().rstrip()

# n : 저장된 사이트 주소의 수
# m : 비밀번호를 찾으려는 사이트 주소의 수
n, m = map(int, readText().split())


# help(dict) 출력결과
# class dict(object)
#  |  dict() -> new empty dictionary
#  |  dict(mapping) -> new dictionary initialized from a mapping object's
#  |      (key, value) pairs
#  |  dict(iterable) -> new dictionary initialized as if via:
#  |      d = {}
#  |      for k, v in iterable:
#  |          d[k] = v
#  |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
#  |      in the keyword argument list.  For example:  dict(one=1, two=2)
#  |
#  (중략)


# dict 클래스에 이터러블 객체를 인자로 넣으면 그 객체를 딕셔너리 타입으로 변환시킴
# readText().split() for _ in range(n) : (사이트, 비밀번호)값을 가진 제너레이터 객체를 만드는 코드
# 제너레이터(Generator) : 이터레이터 함수를 만드는 함수
# 이터레이터(Iterator) : 값을 차례대로 꺼낼 수 있는 객체
obj = dict(readText().split() for _ in range(n))
print(readText().split() for _ in range(n))
print(obj)

# 사이트 이름 호출 및 비밀번호 출력
for _ in range(m):
  site = readText()
  print(obj.get(site))