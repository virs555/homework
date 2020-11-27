dialogs = {'Привет':'Привет, человек!', 'Как дела?':'Нормально', 'Что делаешь?':'Кручу вентиляторами'}

def ask_user (dialogs):
    
    while True:
        say = input('Говорите: ')
        print(dialogs.get(say.capitalize, 'Этого я не понимаю (='))

ask_user(dialogs)            