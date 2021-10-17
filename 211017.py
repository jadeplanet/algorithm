def solution(phone_number):
    # 입력받은 문자열을 한 글자씩 나누어 arr 리스트에 저장
    arr = list(phone_number)

    # arr 리스트의 뒤에서 4번째 까지의 요소만 제외하고
    # 모두 '*'문자열로 변환하기   
    for i in range(len(arr)-4):
        arr[i] = '*'

    # arr 리스트의 요소를 모두 합쳐서 반환 
    return ''.join(arr)


# 만약 입력받은 전화번호 형식이 "010-3333-4444"이었다면..?
# def solution(phone_number):
#     numbers = phone_number.split('-')

#     container = []
#     for item in numbers:
#         container.append(list(item))

#     for i in range(len(container)-1):
#         for j in range(len(container[i])):
#             container[i][j] = '*'

#     answer = []
#     for elem in container:
#         result = ''.join(elem)
#         answer.append(result)

#     return '-'.join(answer)