# 문자열 입력받기
text = input()

# 입력받은 문자열을 한 글자씩 리스트에 저장
container = list(text)

# 인덱스를 하나씩 늘려나가며 문자열 슬라이스하여 리스트에 저장
for i in range(1, len(text)):
    for j in range(len(text)-i):
        container.append(text[j:i+j+1])

# 중복된 값 제거
answer = set(container)

# 결과값의 개수 반환
print(len(answer))