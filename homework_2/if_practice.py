age = int(input('Введите свой возраст '))

def what_to_do(age):
    if age <= 6:
        return "Ты должен быть в детском саду"
    elif 7 <= age <= 16:
        return "Ты должен быть в школе"
    elif 16 <= age <= 21:
        return "Ты должен быть в институте"
    else:
        return "Ты должен работать"

print(what_to_do(age))