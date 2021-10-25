# 입력받은 문자열을 첫 번째 마이너스 기호(-)가 나오는 지점을 기준으로 이등분
s = input().split('-')

# ‘50+40+30-20-100-10+20-30’과 같은 문자열이 주어진다면, split 결과는 다음과 같다.
# [’50+40+30’, ’20’, ‘100’, ’10+20’, ’30’]

# 여기에서 리스트의 첫 번째 원소는 더 이상 값을 작게 만들 수 없다.
# 첫 번째 원소의 덧셈 연산을 수행하고 그 결과를 plus_part 변수에 할당한다.
plus_part = 0
for i in s[0].split('+'):
    plus_part += int(i)

minus_part = 0
for i in s[1:]:
    for j in i.split('+'):
        minus_part += int(j)

print(plus_part - minus_part)


# 아래와 같은 코드로도 작성 가능

# s = input().split('-')

# plus_part = sum(map(int, s[0].split('+')))
# minus_part = sum(list(sum(map(int, item.split('+'))) for item in s[1:]))

# print(plus_part - minus_part)