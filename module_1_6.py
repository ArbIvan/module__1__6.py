# 2. Работа со словарями:
my_dict = {'Ivan': 1984, 'Sergey': 1987, 'Maksim': 1983}
print(my_dict)
print(my_dict['Sergey'])
print(my_dict.get('Bob'))
my_dict.update({'Sasha': 1977, 'Alex': 1979})
print(my_dict)
c = my_dict.pop('Ivan')
print(my_dict)
print(c)

# 3. Работа с множествами:
my_set = {3, 4, 5, 3, (7, 8, 9), False, 'Ivan', 4, False, 'Ivan', (7, 8, 9)}
print(my_set)
print(my_set.add(1))
print(my_set.add(23))
print(my_set)
print(my_set.discard((7, 8, 9)))
print(my_set)