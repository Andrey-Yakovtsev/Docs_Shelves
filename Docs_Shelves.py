from pprint import pprint

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def move_document_by_number(document):
    '''
     m – move – команда, которая спросит номер документа и целевую полку
     и переместит его с текущей полки на целевую.
     '''
    shelves_count = len(directories)
    doc_number = input('Введите номер документа, который надо переместить: ')

    for item in documents:
        if item['number'] == doc_number:
            for keys, values in directories.items():
                if values.count(str(doc_number)) != 0:
                    print(f'Нашел документ на полке {keys}')
                    break
            break
    else:
        print("Документа с указанным номером не существует. Проверьте правильность ввода и повторите")
        shevles_finder_by_number(directories)

    shelf_number = int(input(f'Введите номер полки на которую перемещаем цифрой (от 1 до {shelves_count}):'))
    if not 1 <= int(shelf_number) <= shelves_count:
        print("Такой полки не существует. Проверьте правильность ввода и повторите")
        print()
        move_document_by_number(directories)

    else:
        for keys, values in directories.items():
            try:
                values.remove(doc_number)
            except ValueError:
                pass
            else:
                (directories[str(shelf_number)]).append(doc_number)
                print(f'Документ стоит на {int(shelf_number)} полке. Проверяем:')
                pprint(directories.items())
                break


def doc_finder_by_number(document):
    '''
    # p - для поиска пользователя по номеру документа
    '''
    doc_number = input('Для определения фамилии введите номер документа: ')

    for document in documents:
        if document.get('number') == doc_number:
            print(document.get('name'))
            print()
            break
    else:
        print("Документа с указанным номером не существует.Проверьте правильность ввода и повторите")
        print()
        doc_finder_by_number(documents)


def shevles_finder_by_number(document):
    '''
   s - поиск полки по номеру документа.
    '''
    doc_number = input('Для определения полки введите номер документа: ')
    docs_list = []
    for item in documents:
        docs_list.append(item.get("number"))

    if not doc_number in docs_list:
        print("Документа с указанным номером не существует. Проверьте правильность ввода и повторите")
        shevles_finder_by_number(directories)
    else:
        for keys, values in directories.items():
            for number in values:
                if number == doc_number:
                    print()
                    print(f'Документ находится на полке: {keys}')
                    print()
                    break


def all_docs_list():
    '''
     l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"
     '''
    for items in documents:
        print(list(items.values()))


def add_new_doc(new_dict_in_documents):
    '''
    a – add – команда, которая добавит новый документ в каталог и в перечень полок,
    спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
    '''
    doc_number = input("Для добавления нового документа введите: 1) Номер документа: ")
    doc_type = input('2) Тип документа (passport, invoice или insurance): ')
    user_name = input('3) Фамилию и имя (через пробел): ')

    newdict = {}
    newdict["number"] = doc_number
    newdict["type"] = doc_type
    newdict["name"] = user_name
    documents.append(newdict)
    print(f' Вы добавили в архив новый документ со значениями:'
          f' "number" = {doc_number}, "type" = {doc_type}, "name" = {user_name}. '
          f'В базе это выглядит так:')
    pprint(documents[-1])

    def check_shelf(shelf_number):
        shelves_count = len(directories)
        shelf_number = int(input(f'4) Номер полки цифрой (от 1 до {shelves_count})'))
        if 1 <= shelf_number <= shelves_count:
            directories[str(shelf_number)].append(doc_number)
            print(directories)
        else:
            print("Введен неверный номер полки, повторите ввод")
            check_shelf(shelf_number)

    check_shelf(directories)


def doc_delete_by_number(document):
    '''
    # d - для удаления пользователя по номеру документа
    '''
    docs_list = []
    for item in documents:
        docs_list.append(item.get("number"))

    doc_number = input('Для удаления документа введите его номер: ')
    if not doc_number in docs_list:
        print("Документа с указанным номером не существует. Проверьте правильность ввода и повторите")

    else:
        for docs in documents:
            if docs["number"] == str(doc_number):
                print(f'Удален документ {docs["name"]}')
                print()
                documents.remove(docs)

        for docums in directories.values():
            i = 0
            for item in docums:
                if item == doc_number:
                    docums.remove(item)
                    i += 1
        pprint(f' Проверяем оставшийся список документов {documents}')
        pprint(f' Проверяем оставшийся список директорий {directories}')


def add_new_shelf(shelf_number):
    '''
    # as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.
    Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.;
    '''
    shelves_count = len(directories)
    shelf_number = input(f'Для добавления полки введите следующий порядковый'
                         f' номер за пределеами значений от 1 до {shelves_count}: ')
    if 1 <= int(shelf_number) <= shelves_count:
        print("Такая полка уже существует. Проверьте правильность ввода")
        add_new_shelf(directories)
    elif int(shelf_number) > (shelves_count + 1):
        print(f'Номер новой полки не соответствует порядку. '
              f'Введите следующий порядковый. Подсказка: {shelves_count + 1}')
        add_new_shelf(directories)
    elif int(shelf_number) < 1:
        print(f'Номер новой полки не соответствует порядку. '
              f'Введите следующий порядковый. Подсказка: {shelves_count + 1}')
        add_new_shelf(directories)
    else:
        directories.update({shelf_number: []})
        print(f'Полка с номером {shelf_number} успешно создана')
        print()


def person_lookup():
    '''
    lp - look person - выводит имена всех владельцев документов из базы
    '''
    i = 0
    for docs in directories.values():
        for item in docs:
            if item == documents[i]['number']:
                print(f'Документ {documents[i]["number"]} принадлежит {documents[i]["name"]}')
                i += 1
            else:
                print("Документ не имеет владельца")


def main():
    while True:
        user_input = input(
            'Введите команду: \n '
            'p - для поиска пользователя по номеру документа,\n '
            's - для поиска полки по номеру документа, \n '
            'l - вывод всех документов,\n '
            'lp - выводит имена всех владельцев документов из базы, \n'
            'a - для добавления новых данных, \n '
            'd - для удаления документа из каталога и перечня полок по номеру, \n '
            'm - для перемещения между полками \n '
            'as - для добавления новой полки, \n '
            'q - для выхода): '
        )
        if user_input == 'p':
            doc_finder_by_number(documents)
        elif user_input == 's':
            shevles_finder_by_number(directories)
        elif user_input == 'l':
            all_docs_list()
        elif user_input == 'a':
            add_new_doc(documents)
        elif user_input == 'd':
            doc_delete_by_number(documents)
        elif user_input == 'm':
            move_document_by_number(directories)
        elif user_input == 'as':
            add_new_shelf(directories)
        elif user_input == 'lp':
            person_lookup()
        elif user_input == 'q':
            break


main()
