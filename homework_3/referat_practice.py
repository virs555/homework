with open('referat.txt', 'r', encoding='utf-8') as myfile:
    content = myfile.read()
    print(content) # Текст
    print(len(content)) # Кол-во знаков
    content = content.replace('.','!') # Меняем точки на воскл. знаки

with open('referat2.txt', 'w', encoding='utf-8') as myfile:
    myfile.write(content)
    