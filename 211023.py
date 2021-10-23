from functools import reduce

def solution(number):
    # 숫자형 데이터 => 문자형 데이터 변환 후 한 글자씩 나누어 리스트에 저장
    str_list = list(str(number))

    # 리스트 내부의 문자형 데이터 엘리먼트들을 숫자형으로 형변환 후 새로운 리스트에 저장
    digit_list = [int(item) for item in str_list]

    # 리스트에 있는 모든 엘리먼트의 합 구하기
    sum_digit = reduce(lambda x,y: x+y, digit_list)

    # 값의 정수 여부를 판단하는 함수 선언
    def is_int(value):
        return value == int(value)

    # 하샤드 수 판단 결과 반환
    return is_int(number / sum_digit)