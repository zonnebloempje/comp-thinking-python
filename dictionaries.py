my_dict = {
    'Alex': 32,
    'Bob': 28,
    'Monica': 27,
    'Erika': 43
}
print(my_dict)

print(my_dict['Monica'])
print(my_dict.get('Juan Carlos', 30)) # 30 is the default value

my_dict['Bob'] = 29
print(my_dict)

my_dict['Juan Carlos'] = 60
print(my_dict)

#Delete
del my_dict['Alex']
print(my_dict)


#Prints the keys
for key in my_dict.keys():
    print(key)

#Prints the values
for value in my_dict.values():
    print(value)

#Prints the key and the value
for key, value in my_dict.items():
    print(key, value)

print('Juan Carlos' in my_dict) #True because it is in the dictionary
print('Juan Pablo' in my_dict) # False because it is not in the dictionary