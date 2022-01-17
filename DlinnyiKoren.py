# Позднее решу с помощью длинной арифметики)

#еще не решил

number = int(input())
temp = number ** 0.5
answer = round(temp)

# print(answer)
if answer ** 2 <= number:
    print(answer)
else:
    print(answer-1)


