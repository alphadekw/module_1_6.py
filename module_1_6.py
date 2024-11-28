my_dict = {'Vlad': 2007, 'Maks': 2005, 'Anton': 2006}
print(my_dict)
print(my_dict['Vlad'])
print(my_dict.get('Katya'))

my_dict['Vadim'] = 2000
my_dict['Liza'] = 2001
print(my_dict)

del my_dict['Maks']
print(my_dict)

#множество

my_set = {1, 2, 2, 1, 3, 3, 3}
print(my_set)

(my_set.add(6))
(my_set.add(7))
print(my_set)

(my_set.discard(2))
print(my_set)

delete = my_set.pop()
print(my_set)
