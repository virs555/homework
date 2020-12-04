# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
# ???
students_to_dict = {}
for student in students:
    if student['first_name'] in students_to_dict:
        students_to_dict[student['first_name']] += 1
    else:
        students_to_dict[student['first_name']] = 1
    
print(students_to_dict) #Не совсем то, что в примере вывода, можно ли как-то вывести словарь построчно без for? Как с for я знаю
print('-------------------------')
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
# ???
students_to_dict = {}
for student in students:
    if student['first_name'] in students_to_dict:
        students_to_dict[student['first_name']] += 1
    else:
        students_to_dict[student['first_name']] = 1

print(f'Самое популярное имя среди учеников : {max(students_to_dict, key=students_to_dict.get)}') #Кое-как нагуглил max, get () нужен со скобками или без?
print('-------------------------')
# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
# ???
count = 0
for student in school_students:
  students_to_dict_1 = {}
  count += 1
  for i in student:
    if i['first_name'] in students_to_dict_1:
      students_to_dict_1[i['first_name']] += 1
    else:
      students_to_dict_1[i['first_name']] = 1
  print(f'Самое популярное имя среди учеников класса {count} : {max(students_to_dict_1, key=students_to_dict_1.get)}')
print('-------------------------')


# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???
for classes in school:
  classes_gender = {'male':0, 'female':0, 'class':classes['class']}
  classes_gender['class'] = classes['class']
  for student in classes['students']:
    if is_male[student['first_name']]:
      classes_gender['male'] += 1
    else:
      classes_gender['female'] += 1
  print(f'В классе {classes_gender["class"]} : Мальчиков - {classes_gender["male"]}, Девочек - {classes_gender["female"]}')
        
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.
print('-------------------------')

# Задание 5 НЕ ВЫПОЛНИЛ
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???
classes_gender_male = {}
classes_gender_female = {}
for classes in school:
  for student in classes['students']:
    if is_male[student['first_name']]:
      if classes['class'] in classes_gender_male.keys():
        classes_gender_male[classes['class']] += 1
      else:
        classes_gender_male[classes['class']] = 1
    else:
      if classes['class'] in classes_gender_female.keys():
        classes_gender_female[classes['class']] += 1
      else:
        classes_gender_female[classes['class']] = 1

max_gender_count = 0
max_male =""
max_female = ""
for i in classes_gender_male:
  if classes_gender_male[i] > max_gender_count:
    max_male = i
  print(f'Больше всего мальчиков в классе {max_male}') 

max_gender_count = 0

for i in classes_gender_female:
  if classes_gender_female[i] > max_gender_count:
    max_female = i
  print(f'Больше всего мальчиков в классе {max_female}') 

#НЕ ВЫПОЛНИЛ
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a