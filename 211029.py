# Memory :  49308KB , Time : 5676ms

from sys import stdin

case_number = int(stdin.readline())

for _ in range(case_number):
    candidates_number = int(stdin.readline())
    grade_list = []
    pass_count = 0

    for _ in range(candidates_number):
        grade = list(map(int, stdin.readline().split()))
        grade_list.append(grade)

    grade_list.sort()
    least_interview_rank = grade_list[0][1]

    for i in range(candidates_number):
        if grade_list[i][1] <= least_interview_rank:
            pass_count += 1
            least_interview_rank = grade_list[i][1]

    print(pass_count)
