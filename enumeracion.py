object = int(input('Pick an integer: '))
answer = 0

while answer ** 2 < object:
   # print(answer)
    answer += 1

if answer ** 2 == object:
    print(f'Square root of {object} is {answer}')
else:
    print(f'{object} is not a perfect square')