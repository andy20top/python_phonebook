import os

def print_data():
    with open("phonebook.txt", 'r', encoding='utf-8') as file:
        contacts_list = file.read().rstrip().split("\n\n")
    for num_line, line in enumerate(contacts_list, 1):
        print((f"{num_line} {line}"))

def input_name():
    return input("Введите имя: ").title()

def input_surname():
    return input("Введите фамилию: ").title()

def input_patronomic():
    return input("Введите отчетство: ").title()

def input_phone():
    return input("Введите телефон: ")

def input_address():
    return input("Введите адрес: ").title()

def input_data():
    surname = input_surname()
    name = input_name()
    patronomic = input_patronomic()
    phone = input_phone()
    address = input_address()
    my_sep = ' '
    return f"{surname}{my_sep}{name}{my_sep}{patronomic}{my_sep}{phone}\n{address}\n\n"

def add_contact():
    new_contact_str = input_data()
    with open("phonebook.txt", 'a', encoding='utf-8') as file:
        file.write(new_contact_str)

def search_contact():
    print("Варианты поиска:\n"
          "1. По фамилии\n"
          "2. По имени\n"
          "3. По отчеству\n"
          "4. По телефону\n"
          "5. По адресу\n")
    command = input("Выберите вариант поиска: ")
    while command not in ("1", "2", "3", "4", "5"):
        print("Некорректный ввод")
        command = input("Выберите вариант поиска: ")

    i_search = int(command) - 1
    search = input("Введите данные для поиска: ").lower()
    with open("phonebook.txt", 'r', encoding='utf-8') as file:
        contacts_list = file.read().rstrip().split("\n\n")
    check_cont = False
    for contact_str in contacts_list:
        lst_contact = contact_str.lower().replace("\n", " ").split()
        if search in lst_contact[i_search]:
            print(contact_str)
            check_cont = True
    if not check_cont:
        print("Контакт не найден")


def copy_contact():
    i_copy = int(input("Введите номер строки, которую необходимо скопировать: "))
    with open("phonebook.txt", 'r', encoding='utf-8') as file:
        contacts_list = file.read().rstrip().split("\n\n")
    for num_line, line in enumerate(contacts_list, 1):
        if num_line == i_copy:
            with open('new_phonebook.txt', 'a', encoding='utf-8') as new_file:
                new_file.write(f"{line}\n\n")


def interface():
    with open("phonebook.txt", 'a', encoding='utf-8'):
        pass
    command = ""
    while command != "5":
        print("Меню пользователя:\n"
              "1. Вывод данных на экран\n"
              "2. Добавить контакт\n"
              "3. Поиск контакта\n"
              "4. Копирование контакта\n"
              "5. Выход\n")
        command = input("Выберите пункт меню: ")

        while command not in ("1", "2", "3", "4", "5"):
            print("Некорректный ввод")
            command = input("Выберите пункт меню: ")

        match command:
            case "1":
                print_data()
            case "2":
                add_contact()
            case "3":
                search_contact()
            case "4":
                copy_contact()
            case "5":
                print("Завершение программы")

if __name__ == "__main__":
    interface()
