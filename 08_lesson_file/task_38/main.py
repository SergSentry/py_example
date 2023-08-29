#
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

from os.path import exists

CONTACT_NUMBER = 'number'
FIRST_NAME = 'first_name'
LAST_NAME = 'last_name'
MIDDLE_NAME = 'middle_name'
PHONE_NUMBER = 'phone_number'

FIELD_DELIMITER = ';'

FILE_NAME = 'contacts.txt'

MAIN_MENU_ADD = 1
MAIN_MENU_SAVE = 2
MAIN_MENU_PRINT = 3
MAIN_MENU_SEARCH = 4
MAIN_MENU_LOAD = 5
MAIN_MENU_CHANGE = 6
MAIN_MENU_REMOVE = 7
MAIN_MENU_EXIT = 8

MAIN_MENU = f'{MAIN_MENU_ADD}. Add  {MAIN_MENU_SAVE}. Save  {MAIN_MENU_PRINT}. Print  {MAIN_MENU_SEARCH}. \
Search  {MAIN_MENU_LOAD}. Load  {MAIN_MENU_CHANGE}. Change  {MAIN_MENU_REMOVE}. Remove  {MAIN_MENU_EXIT}. Exit'

SEARCH_MENU_LAST_NAME = 1
SEARCH_MENU_FIRST_NAME = 2
SEARCH_MENU_PHONE_NUMBER = 3
SEARCH_MENU_EXIT = 4

SEARCH_MENU = f'{SEARCH_MENU_LAST_NAME}. Last name  {SEARCH_MENU_FIRST_NAME}. First name  {SEARCH_MENU_PHONE_NUMBER}. \
Phone  {SEARCH_MENU_EXIT}. Exit'


CHANGE_MENU_LAST_NAME = 1
CHANGE_MENU_FIRST_NAME = 2
CHANGE_MENU_MIDDLE_NAME = 3
CHANGE_MENU_PHONE_NUMBER = 4
CHANGE_MENU_EXIT = 5

CHANGE_MENU = f'{CHANGE_MENU_LAST_NAME}. Last name  {CHANGE_MENU_FIRST_NAME}. First name  {CHANGE_MENU_MIDDLE_NAME}. \
Middle name  {CHANGE_MENU_PHONE_NUMBER}. Phone  {CHANGE_MENU_EXIT}. Exit'


def show_menu(menu: str, min_menu_item: int, max_menu_item: int, default_choice: int) -> int:
    while True:
        print(100*'-')
        print()
        print(menu)
        choice = input(f'choose [{min_menu_item}-{max_menu_item}]: ')
        if choice == '':
            return default_choice
        if choice.isdigit():
            choice_value = int(choice)
            if min_menu_item <= choice_value <= max_menu_item:
                return choice_value


def load_from_file(filename: str) -> list[dict[str, str]]:
    contacts = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        index = 0
        for contactLine in lines:
            last_name, first_name, middle_name, phone_number = contactLine.strip().split(FIELD_DELIMITER)
            contacts.append({
                CONTACT_NUMBER: index,
                LAST_NAME: last_name,
                FIRST_NAME: first_name,
                MIDDLE_NAME: middle_name,
                PHONE_NUMBER: phone_number
            })
            index += 1

    return contacts


def save_to_file(filename: str, contacts):
    with open(filename, 'w') as file:
        for contact in contacts:
            file.write(f"{contact[LAST_NAME]}{FIELD_DELIMITER}{contact[FIRST_NAME]}{FIELD_DELIMITER}{contact[MIDDLE_NAME]}{FIELD_DELIMITER}{contact[PHONE_NUMBER]}\n")


def print_contacts(contacts: list[dict[str, str]]):
    for index, contact in enumerate(contacts, start=1):
        print(
            f"{index}. {contact[LAST_NAME]}, {contact[FIRST_NAME]}, {contact[MIDDLE_NAME]}, ph:{contact[PHONE_NUMBER]}")


def search_contacts(contacts: list[dict[str, str]], column: str, value: str):
    results = []
    for contact in contacts:
        if value.lower() in contact[column].lower():
            results.append(contact)
    return results


def input_contact():
    last_name = input('Input last name: ')
    first_name = input('Input first name: ')
    middle_name = input('Input middle name: ')
    phone_number = input('Input phone number: ')
    return last_name, first_name, middle_name, phone_number


def add_contact(contacts: list[dict[str, str]], last_name: str, first_name: str, middle_name: str, phone_number: str):
    contact = {
        LAST_NAME: last_name,
        FIRST_NAME: first_name,
        MIDDLE_NAME: middle_name,
        PHONE_NUMBER: phone_number
    }
    contacts.append(contact)


def add_contact_handler(contacts: list[dict[str, str]]):
    last_name, first_name, middle_name, phone_number = input_contact()
    add_contact(contacts, last_name, first_name, middle_name, phone_number)
    print('Contact appended\n')


def save_contact_handler(contacts: list[dict[str, str]]):
    save_to_file(FILE_NAME, contacts)
    print('Contacts saved\n')


def print_contact_handler(contacts: list[dict[str, str]]):
    print('\nContacts:')
    print_contacts(contacts)
    print()


def search_contact_handler(contacts: list[dict[str, str]]):
    while True:
        results = []
        choice = show_menu(SEARCH_MENU, SEARCH_MENU_LAST_NAME, SEARCH_MENU_EXIT, SEARCH_MENU_EXIT)
        if choice == SEARCH_MENU_LAST_NAME:
            value = input("Input last name: ")
            results = search_contacts(contacts, LAST_NAME, value)
        elif choice == SEARCH_MENU_FIRST_NAME:
            value = input("Input first name: ")
            results = search_contacts(contacts, FIRST_NAME, value)
        elif choice == SEARCH_MENU_PHONE_NUMBER:
            value = input("Input phone: ")
            results = search_contacts(contacts, PHONE_NUMBER, value)
        elif choice == SEARCH_MENU_EXIT:
            return
        else:
            return

        if results:
            print('Find contacts: ')
            print_contacts(results)
        else:
            print('No contacts found')


def load_contact_handler():
    if exists(FILE_NAME):
        contacts = load_from_file(FILE_NAME)
        print(f"\nLoaded {len(contacts)} contacts")
        return contacts
    print('File contacts.txt not found')


def change_contact_handler(contacts: list[dict[str, str]]):
    index = int(input("Input index number for change contact, or 0 to exit: "))
    if index == 0:
        return
    elif 1 <= index <= len(contacts):
        contact = contacts[index - 1]
        print(f"You choose.\n {contact[LAST_NAME]}, {contact[FIRST_NAME]}, {contact[MIDDLE_NAME]}, ph:{contact[PHONE_NUMBER]}")
        while True:
            choice = show_menu(CHANGE_MENU, CHANGE_MENU_LAST_NAME, CHANGE_MENU_EXIT, CHANGE_MENU_EXIT)
            if choice == CHANGE_MENU_LAST_NAME:
                value = input("Input last name: ")
                contact[LAST_NAME] = value
            elif choice == CHANGE_MENU_FIRST_NAME:
                value = input("Input first name: ")
                contact[FIRST_NAME] = value
            elif choice == CHANGE_MENU_MIDDLE_NAME:
                value = input("Input middle name: ")
                contact[MIDDLE_NAME] = value
            elif choice == CHANGE_MENU_PHONE_NUMBER:
                value = input("Input phone: ")
                contact[PHONE_NUMBER] = value
            elif choice == SEARCH_MENU_EXIT:
                return
            else:
                return


def remove_contact_handler(contacts):
    index = int(input("Input index number for remove contact, or 0 to exit: "))
    if index == 0:
        return
    elif 1 <= index <= len(contacts):
        contact = contacts[index - 1]
        print(f"You choose.\n {contact[LAST_NAME]}, {contact[FIRST_NAME]}, {contact[MIDDLE_NAME]}, ph:{contact[PHONE_NUMBER]}")
        yon = input("\npress y for delete contact [n]: ")
        if yon.lower() == 'y':
            contacts.remove(contact)


def exit_handler():
    print()


def main():
    phonebook = []

    while True:
        choice = show_menu(MAIN_MENU, MAIN_MENU_ADD, MAIN_MENU_EXIT, MAIN_MENU_EXIT)
        if choice == MAIN_MENU_ADD:
            add_contact_handler(phonebook)
        elif choice == MAIN_MENU_SAVE:
            save_contact_handler(phonebook)
        elif choice == MAIN_MENU_PRINT:
            print_contact_handler(phonebook)
        elif choice == MAIN_MENU_SEARCH:
            search_contact_handler(phonebook)
        elif choice == MAIN_MENU_LOAD:
            phonebook = load_contact_handler()
        elif choice == MAIN_MENU_CHANGE:
            change_contact_handler(phonebook)
        elif choice == MAIN_MENU_REMOVE:
            remove_contact_handler(phonebook)
        elif choice == MAIN_MENU_EXIT:
            exit_handler()
            break
        else:
            break


if __name__ == '__main__':
    main()
