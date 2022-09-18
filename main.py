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


def name_output(documents, number):
    count = False
    # number = input("Введите номер документа:\n")
    for doc in documents:
        if number == doc["number"]:
            count = True
            break
    if count == True:
        return doc["name"]
    else:
        print("Введен неверный номер документа")


def dir_output(directories, number):
    count = False
    # number = input("Введите номер документа:\n")
    for shelf, dir in directories.items():
        if number in dir:
            count = True
            break
    if count == True:
        return shelf
    else:
        print("Введен неверный номер документа")


def ListAllDoc(documents):
    list_dict = []
    for list_doc in documents:
        list_dict.append(list_doc["type"])
        list_dict.append(list_doc["number"])
        list_dict.append(list_doc["name"])
    return list_dict


def addition(documents, directories, name, type, number, direct):
    document = {}
    # name = input("Введите имя владельца:\n")
    # type = input("Введите тип документа:\n")
    # number = input("Введите номер документа:\n")
    count = False
    # direct = input("Введите номер полки:\n")
    for dir in directories:
        if direct == dir:
            directories[dir] += [number]
            count = True
            break
    if count == True:
        document.setdefault("type", type)
        document.setdefault("number", number)
        document.setdefault("name", name)
        documents.append(document)
        return documents, directories
    else:
        print("Такой полки не существует")


def delete_number(documents, directories, number):
    documents1 = documents.copy()
    count = False
    # number = input("Введите номер документа для удаления:\n")
    for doc in documents1:
        if doc["number"] == number:
            documents.remove(doc)
            count = True
            break
    if count == False:
        print("Такого номера не существует")
        return
    for dir in directories:
        if number in directories[dir]:
            (directories[dir]).remove(number)
    return documents, directories


def traffic(directories, number, direct):
    count = False
    count2 = False
    dir_ = []
    temp = None
    # number = input("Введите номер документа:\n")
    # direct = input("Введите номер полки для перемещения:\n")

    for dir, num in directories.items():
        if number in num:
            temp2 = (directories[dir]).index(number)
            temp = (directories[dir]).pop(temp2)
    if temp == None:
        print("Такого номера документа нет")

    for dir in directories:
        dir_.append(dir)
    if direct not in dir_:
        print("Такого номера полки нет")
    else:
        directories[direct] += [temp]
        directories.setdefault(direct, [temp])
        print(directories)
        return directories


def new_shelf(directories, direct):
    # direct = input("Введите номер новой полки :\n")
    dir_ = []
    for dir in directories:
        dir_.append(dir)
    if direct in dir_:
        print("Такая полка уже есть")
    else:
        directories.update({direct: []})
        return directories


def main(documents, directories):
    """
        ap - (all people) - команда, которая выводит список всех владельцев документов
        p – (people) – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
        l – (list) – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
        s – (shelf) – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
        a – (add) – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,
        имя владельца и номер полки, на котором он будет храниться.
        d – (delete) – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
        m – (move) – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
        as – (add shelf) – команда, которая спросит номер новой полки и добавит ее в перечень;
        q - (quit) - команда, которая завершает выполнение программы
        """
    while True:
        command = input("Введите команду:\n")
        if command == "p":
            name_output(documents, number)
        elif command == "s":
            dir_output(directories, number)
        elif command == "l":
            ListAllDoc(documents)
        elif command == "a":
            addition(documents, directories, name, type_, number, direct)
        elif command == "d":
            delete_number(documents, directories, number)
        elif command == "m":
            traffic(directories, number, direct)
        elif command == "as":
            new_shelf(directories, direct)
        elif command == "q":
            print("Выход")
            break


if __name__ == '__main__':
    main(documents, directories)
