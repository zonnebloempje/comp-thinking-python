# Unlike lists, tuples are immutable, but you can reasign the variable to a new tuple:
my_tuple = (1, 2, 3)
my_other_tuple = (4, 5, 6)
print('MY TUPLE: ')
print('First result: ', my_tuple)
my_tuple += my_other_tuple
print('Second result: ', my_tuple)
print(type(my_tuple))

x, y ,z = my_other_tuple

print(y)
print(z)
print(x)
