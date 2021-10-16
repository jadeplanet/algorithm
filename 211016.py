def solution(str, num):
    # 입력받은 문자열을 아스키코드로 변환 후 asciiList에 저장하기
    asciiList = []
    for i in range(len(str)):
        # 문자열이 소문자일 경우
        if str[i].islower():
            # 새로운 아스키코드 값 
            newAscii = ord(str[i]) + num
            
            # 새로운 아스키코드 값이 알파벳 소문자의 범위(97~122)를 넘어갈 경우
            # 첫 번째 소문자(a)로 되돌아가기
            if newAscii > 122:
                newAscii -= 26
            asciiList.append(newAscii)

        # 문자열이 대문자일 경우
        if str[i].isupper():
            # 새로운 아스키코드 값
            newAscii = ord(str[i]) + num

            # 새로운 아스키코드 값이 알파벳 대문자의 범위(65~90)를 넘어갈 경우
            # 첫 번째 대문자(A)로 되돌아가기
            if newAscii > 90:
                newAscii -= 26
            asciiList.append(newAscii)
        
        # 문자열이 공백문자일 경우
        if str[i] == ' ':
            # 공백문자에 대응하는 아스키코드인 32를 asciiList에 추가
            asciiList.append(32)

    answer = []
    for i in range(len(asciiList)):
        # 새로운 아스키코드 리스트의 요소들을 문자열로 변환하여 answer 리스트에 추가
        newCode = chr(asciiList[i])
        answer.append(newCode)

    # answer 리스트의 요소들을 문자열로 합쳐서 반환
    return ''.join(answer)