# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
# ???
for name in names:
    print(name)

# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём.

names = ['Оля', 'Петя', 'Вася', 'Маша']
# ???
for name in names:
    print(f'{name}  {len(name)}')


# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
# ???
for name in names:
  if is_male.get(name) is True:
    print(f'{name}: Мужской')
  elif is_male.get(name) is False:
    print(f'{name}: Женский')
  else:
    print('Некорректное значение пола')

# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# В группе 2 ученика.
# В группе 3 ученика.

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
# ???
print(f'Всего групп: {len(groups)}')
group_counter = 0
for group in groups:
  group_counter += 1
  print(f'В группе {group_counter} количество учеников: {len(group)}')

# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят.
# Пример:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
# ???
group_counter = 0
for group in groups:
  group_counter += 1
  print(f'Группа {group_counter}: {", ".join(group)}') # Тут наверное нужно было как-то иначе делать, т.к. join мы не проходили, подглядел в Гугле