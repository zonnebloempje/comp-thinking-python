def divide_list_elements(list, divisor):
    try:
        return [i / divisor for i in list]
    except ZeroDivisionError as e:
        print(e)
        return list
    
list = list(range(10))
divisor = 1 #division by zero

print(divide_list_elements(list, divisor))
