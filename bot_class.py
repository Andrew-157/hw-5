from collections import UserDict


class Field:
    pass


class Name:
    def __init__(self, name):
        self.value = name


class Phone:
    def __init__(self, phone):
        self.value = phone


class Record:
    def __init__(self, name, phone=None):
        self.name = Name(name)
        if phone:
            self.phones = [Phone(phone)]
        else:
            self.phones = []

    def add(self, name, value):
        address_book[name].phones.append(Phone(value))

    def change(self, name, value):
        address_book[name].phones = [Phone(value)]

    def delete(self, name):
        address_book[name].phones.clear()


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        return self.data


address_book = AddressBook()


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Try again, please"
    return inner


def say_hello():
    return "How can I help you?"


@input_error
def add(data):
    name_ = data.split(" ")[1]

    if len(data.split(" ")) == 2:
        if name_ not in address_book:
            record = Record(name_)
            address_book.add_record(record)
            return f"{name_} was added to Address Book"
        else:
            return f"{name_} is already in Address Book, if you want to add new information, enter: add {name_} 'phone/email'"

    elif len(data.split(" ")) == 3:
        info = data.split(" ")[2]

        if name_ not in address_book:

            record = Record(name_, info)
            address_book.add_record(record)
            return f"{name_} with {info} was added to Address Book"

        else:

            address_book[name_].add(name_, info)
            return f"{info} was added to {name_} in Address Book"

    else:
        return "Using this command, you should only enter the name or name with only one value to be added to Address Book"


@input_error
def change(data):
    name_ = data.split(" ")[1]

    if len(data.split(" ")) < 3:
        return f"Please enter 'change' command again with {name_} and {name_}'s new information"

    elif len(data.split(" ")) > 3:
        return f"Please, enter 'change' command for {name_} again with only one new value"

    else:

        if name_ not in address_book:
            return f"{name_} doesn't have any information in Address Book, call 'add' command instead."

        else:
            info = data.split(" ")[2]
            address_book[name_].change(name_, info)
            return f"{name_}'s information in Address Book was changed to {info}"


@input_error
def info(data):
    name_ = data.split(" ")[1]

    if name_ not in address_book:
        return f"{name_} doesn't have any information in Address Book, you can't see it"
    else:
        info_list = []
        for info in address_book[name_].phones:
            info_list.append(info.value)
        return info_list


@input_error
def delete(data):
    name_ = data.split(" ")[1]

    if name_ not in address_book:
        return f"{name_} doesn't have any information in Address Book, you can't delete it"

    else:

        address_book[name_].delete(name_)
        return f"{name_}'s information was deleted from Address Book"


def show_all():
    human_readable = {}
    for k, v in address_book.items():
        human_readable.update({k: [phone.value for phone in v.phones]})

    return human_readable


COMMANDS = {"hello": say_hello,
            "show all": show_all,
            "add": add,
            "change": change,
            "info": info,
            "delete": delete}


def handler(comm):
    return COMMANDS[comm]


def main():
    while True:
        user_command = input("Enter a command: ")

        if user_command.lower() == "hello" or user_command.lower() == "show all":
            print(handler(user_command.lower())())

        elif user_command.split(" ")[0].lower() not in ["change", "info", "add", "exit", "close", "goodbye", "delete"]:
            print("No such a command")

        elif user_command.lower() in ["exit", "close", "goodbye"]:
            print("Goodbye")
            break

        else:
            print(handler(user_command.split(" ")[0].lower())(user_command))


if __name__ == "__main__":
    main()
