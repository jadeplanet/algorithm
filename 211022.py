n = int(input())
count = 0

# 두 자리 이하의 수는 비교할 자릿수가 없으므로 모두 한수
if n <= 99:
    count = n

else:
    # 100 이상의 자연수에서 한수 찾기
    count = 99
    for i in range(100, n+1):
        i = str(i) # 숫자형을 문자형으로 타입 변환
        digits = [int(item) for item in list(i)] # 문자열을 한 글자씩 나눠서 리스트에 담고, 각 원소를 숫자형으로 변환
        if digits[0] - digits[1] == digits[1] - digits[2]:  # 각 자릿수의 등차수열 여부 확인
            count += 1

print(count)