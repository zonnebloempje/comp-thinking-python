objective = int(input('Pick an integer: '))
epsilon = 0.01
step = epsilon**2
answer = 0.0

while abs(answer**2 - objective) >= epsilon and answer <= objective:
    print(abs(answer**2 - objective), answer)
    answer += step

if abs(answer**2 - objective) >= epsilon:
    print(f'Could not find the square root of {objective}')
else:
    print(f'The square root of {objective} is close to {answer}')