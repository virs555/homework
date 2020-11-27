def hello_user():
    try:
        while True:
            answer = input('Как дела? ')
            answer = answer.capitalize()
            if answer == 'Хорошо':
                break
    except KeyboardInterrupt:
        print('Пока!')
hello_user()
        
