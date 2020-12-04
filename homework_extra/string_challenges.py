# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
# ???
print(word.lower().count('а'))

# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???
eyuioa_count = 0
for i in word:
    if i.lower() in 'уеыаоэяию':
        eyuioa_count += 1
print(eyuioa_count)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???
print(len(sentence.split()))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???
sentense_list = sentence.split()
for i in sentense_list:
    print(i[-1])

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
# ???
sentense_list = sentence.split()
summ = 0
for i in sentense_list:
    summ += len(i)

print(summ/len(sentense_list))
