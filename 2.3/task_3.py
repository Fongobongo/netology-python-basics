documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "passport", "number": "5455 028765"},
    {"type": "passport", "number": "5400 028765"},
    {"type": "passport", "number": "5455 002299"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}


def list_catalog():
    if documents == []:
        print("\nВ базе не зарегистрировано ни одного документа.\n")
        return
    print("\nСписок всех документов:\n")
    for item in documents:
        for key in item:
            print(f"\"{item.get(key)}\"", end=" ")
        print()
    print("\nСписок всех полок:\n")
    for key in directories.keys():
        print(key)
    print()


def show_owner():
    doc_number = input("\nВведите номер документа: ")
    for item in documents:
        if doc_number == item.get("number"):
            print(f"\nВладельцем документа {doc_number} является {item.get('name')}\n")
            break
    else:
        print(f"\nВ каталоге нет документа с номером {doc_number}\n")


def show_shelf():
    doc_number = input("\nВведите номер документа: ")
    for key, value in directories.items():
        for element in value:
            if element == doc_number:
                print(f"\nДокумент {doc_number} находится на полке № {key}\n")
                return
    else:
        print(f"\nДокумент {doc_number} не найден ни на одной из полок.\n")


def add_document():
    new_doc = input(
        "\nВведите (разделяя запятой с пробелом) номер документа, его тип, имя владельца, номер полки: ").split(", ")
    if len(new_doc) == 4:
        for i, item in enumerate(new_doc):
            new_doc[i] = item.strip()
            if bool(new_doc[i]) == False:
                print(f"\nОшибка! Аттрибут № {i + 1} содержит пустое значение '{item}'.\n")
                return
        for value in directories.values():
            for element in value:
                if element == new_doc[0]:
                    print(f"\nДокумент с номером {new_doc[0]} уже существует. Сверьтесь с регистрационным журналом.\n")
                    return
        if new_doc[3] not in directories.keys():
            print(
                f"\nВы не можете положить документ с номером {new_doc[0]} на полку {new_doc[3]}. Такой полки не существует.")
            print("\nСписок имеющихся полок:\n")
            for key in directories.keys():
                print(key)
            agreement = input(
                f"\nХотите сейчас добавить новую полку {new_doc[3]}? Введите Да (или нажмите Enter) если хотите (любой другой ответ будет означать Нет): ").lower()
            if agreement == "да" or agreement == "":
                add_shelf(new_doc[3])
            else:
                print("\nДля добавления новой полки используйте команду as или add shelf.\n")
                return
        documents.append({"type": new_doc[1], "number": new_doc[0], "name": new_doc[2]})
        directories.get(new_doc[3]).append(new_doc[0])
        print(f"\nДокумент {new_doc[1]} c номером {new_doc[0]} добавлен на полку {new_doc[3]}.\n")
    else:
        print("\nВы ошиблись при вводе. Неверное количество агрументов для добавления документа.\n")


def delete_document():
    doc_number = input("\nВведите номер документа, который требуется удалить: ")
    for item in documents:
        if item.get("number") == doc_number:
            documents.remove(item)
            print(f"\nДокумент {doc_number} удалён из базы.\n")
            for key, value in directories.items():
                for element in value:
                    if element == doc_number:
                        value.remove(doc_number)
                        print(f"Документ {doc_number} удалён с полки {key}.\n")
                        return
    else:
        print(f"\nДокумент с таким номером ({doc_number}) в базе не найден.\n")


def move_document():
    moving_doc = input("\nВведите (через запятую с пробелом) номер документа и целевую полку: ").split(", ")
    for doc in documents:
        if doc.get("number") == moving_doc[0]:
            if moving_doc[1] not in directories.keys():
                print(
                    f"\nВы не можете положить документ с номером {moving_doc[0]} на полку {moving_doc[1]}. Такой полки не существует.")
                print("\nСписок имеющихся полок:\n")
                for key in directories.keys():
                    print(key)
                agreement = input(
                    f"\nХотите сейчас добавить новую полку {moving_doc[1]}? Введите Да (или нажмите Enter) если хотите (любой другой ответ будет означать Нет): ").lower()
                if agreement == "да" or agreement == "":
                    add_shelf(moving_doc[1])
                else:
                    print("\nДля добавления новой полки используйте команду as или add shelf.\n")
                    return
            for key, value in directories.items():
                for element in value:
                    if element == moving_doc[0]:
                        if moving_doc[1] == key:
                            print(f"\nДокумент {moving_doc[0]} уже находится на полке {moving_doc[1]}.\n")
                            return
                        directories.get(moving_doc[1]).append(moving_doc[0])
                        directories.get(key).remove(element)
                        print(f"\nДокумент {moving_doc[0]} перемещён на полку {moving_doc[1]}.\n")
                        return
    else:
        print(f"\nДокумент {moving_doc[0]} отсутствует в базе.\n")


def add_shelf(param=False):
    if param is False:
        new_shelf = input("\nВведите номер новой полки: ")
    else:
        new_shelf = param
    if bool(new_shelf.strip()) == False:
        print("\nНельзя добавить новую полку без указания её индентификатора.")
        return
    if new_shelf not in directories.keys():
        directories[new_shelf] = []
        print(f"\nПолка {new_shelf} добавлена.")
    else:
        print(f"\nВы точно туда смотрите? Полка {new_shelf} уже существует!")


def show_all_owners():
    for values in directories.values():
        for item in values:
            for doc in documents:
                if item == doc.get("number"):
                    try:
                        print(f"\nВладельцем документа '{item}' является '{doc['name']}'")
                        break
                    except:
                        print(f"\nВладелец документа '{item}' не определён.")
    print()

def main():
    print(
        "Добро пожаловать в каталог критически важных документов!\n\nВведите h или help для просмотра списка команд.\n")
    while True:
        user_input = input("Введите команду: ")
        if user_input == 'h' or user_input == 'help':
            print("\nСписок команд:", "l (list) – команда, которая выведет список всех документов и полок;",
                  "p (people) – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;",
                  "s (shelf) – команда, которая спросит номер документа и выведет номер полки, на которой он находится;",
                  "a (add) – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться;",
                  "d (delete) – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;",
                  "m (move) – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;",
                  "as (add shelf) – команда, которая спросит номер новой полки и добавит ее в перечень;",
                  "o (owners) – команда, которая выводит имена всех владельцев документов;",
                  "q (quit) - команда, которая завершает работу с программой.\n", sep="\n\n")
        elif user_input == 'l' or user_input == 'list':
            list_catalog()
        elif user_input == 'p' or user_input == 'people':
            show_owner()
        elif user_input == 's' or user_input == 'shelf':
            show_shelf()
        elif user_input == 'a' or user_input == 'add':
            add_document()
        elif user_input == 'd' or user_input == 'delete':
            delete_document()
        elif user_input == 'm' or user_input == 'move':
            move_document()
        elif user_input == 'o' or user_input == 'owners':
            show_all_owners()
        elif user_input == 'as' or user_input == 'add shelf':
            add_shelf()
            print()
        elif user_input == 'q' or user_input == 'quit':
            print("\nВсего хорошего!\n")
            break
        else:
            (print("\nТакой команды не существует, наберите h или help для получения помощи.\n"))


main()