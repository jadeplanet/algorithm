s = input().split('-')

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