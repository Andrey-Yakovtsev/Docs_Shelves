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



shelves_count = len(directories)

doc_number = '10006'
shelf_number = 3
if not 1 <= int(shelf_number) <= shelves_count:
    print("Такой полки не существует.Проверьте правильность ввода и повторите")
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
            print(directories[str(shelf_number)], "содержимое 3й полки")
            break
#         pass
# print(directories.values())
# вызвать стловарь по значению номера полки и доавить туда документ
# print(directories[str(shelf_number)], "содержимое 3й полки")
# new_list = directories[str(shelf_number)]

# print(new_list)
# new_list.append(doc_number)
# print(new_list)
# print(directories[str(shelf_number)], "содержимое 3й полки")