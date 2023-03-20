my_list = [1, 2, 3]

print(my_list)
print(my_list[0]) # 1
print(my_list[1:]) # [2, 3]

my_list.append(4)
print(my_list)

my_list[0] = 'a'
print(my_list)

my_list.pop()
print(my_list)

for element in my_list:
    print(element)

# Side effects of modifying a list
a = [1, 2, 3]
b = a
print(a)
print(b)
print('ID a and b are the same:')
print(id(a))
print(id(b))

c = [a, b]
print(c)

a.append(5)

print(a)
print(c)


#Cloning instead of modifying
a = [1, 2, 3]
print(id(a))
b = a
print(id(b))
c = list(a)
print(id(c))

d = a[::]
print(id(d))

#List comprehension
my_list = list(range(101))
print('my_list 0 - 100: ', my_list)

double = [i * 2 for i in my_list]
print('my_list, but double (i * 2): ', double)

even = [i for i in my_list if i % 2 == 0]
print('my_list, but only even numbers: ', even)