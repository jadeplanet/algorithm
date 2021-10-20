from sys import stdin

# 판매된 티켓값 입력
sold_tickets = int(stdin.readline())

# 판매된 좌석번호 입력
ticket_numbers = list(map(int, stdin.readline().split()))

# 좌석 번호 정렬
ticket_numbers.sort()

# 빈 좌석 찾기
seat_number = 1
while True:
    for occupied in ticket_numbers:
        if seat_number == occupied:
            seat_number += 1
        else:
            # 빈 좌석을 찾았을 경우
            break

    # 빈 좌석 번호 중에서 이미 판매된 번호들보다 작은 번호가 없을 경우
    break

print(seat_number)
