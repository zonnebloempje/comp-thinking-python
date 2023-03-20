# range(start, end, steps)

my_range = range(1, 5)
type(my_range)

for i in my_range:
    print(i)

my_range = range(0, 7, 2)
my_other_range = range(0, 8, 2)

print(my_range == my_other_range) #True

for i in my_range:
    print(i)

for i in my_other_range:
    print(i)

print(id(my_range))
print(id(my_other_range))

print(my_range is my_other_range) #False

print('From 0 to 100, even numbers:')
for i in range(0, 101, 2):
    print(i)

