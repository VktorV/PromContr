import note


def create_note(number):
    title = check_len_text_input(
        input('Введите Название заметки: '), number)
    body = check_len_text_input(
        input('Введите Описание заметки: '), number)
    return note.note(title=title, body=body)


def menu():
    print("\n================ Заметки ================\n\n==== Функции:\n\n1 - показать все заметки\n2 - добавление заметки\n3 - удаление заметки\n4 - редактирование заметки\n5 - показать заметки по дате\n6 - показать заметку по id\n7 - выход\n\nВведите номер функции: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def goodbuy():
    print("Пока! Пока!")
