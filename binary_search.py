objective = int(input('Pick a number: '))
epsilon = 0.01
low = 0.0
high = max(1.0, objective)
answer = (high + low) / 2

while abs(answer**2 - objective) >= epsilon:
    print(f'low= {low}, high= {high}, answer= {answer}')
    if answer**2 < objective:
        low = answer
    else:
        high = answer
    answer = (high + low) / 2
print(f'The square root of {objective} is {answer}')