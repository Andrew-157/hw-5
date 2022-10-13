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
    def __init__(self, name=None, phone=None):
        if phone == None:
            self.name = Name(name)
        else:
            self.name = Name(name)
            self.phone = Phone(phone)

    def __str__(self):
        try:
            return f"{self.name.value}--{self.phone.value}"
        except AttributeError:
            return f"{self.name.value}"

    def change(self, name, info):
        record = Record(name, info)
        address_book.data[record.name.value] = record.__str__()

    def delete(self, name):
        address_book.data.pop(name)

    def delete_all(self):
        address_book.data.clear()


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record.__str__()
        return self.data


address_book = AddressBook()


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Please enter name and phone of the user or only its name"
        except ValueError:
            return "Wrong input"
        except TypeError:
            return "Wrong input"
        except KeyError:
            return "Wrong input"

    return inner


def say_hello():
    return "How can I help you?"


@input_error
def add(data):
    if len(data.split(" ")) == 2:

        name_ = data.split(" ")[1]
        if name_ in address_book.data:
            return f"{name_} already has information, if you want to change it,call 'change' command."

        record = Record(name_)
        address_book.add_record(record)
        return f"{name_} was added"

    else:

        name_ = data.split(" ")[1]
        if name_ in address_book.data:
            return f"{name_} already has information, if you want to change it,call 'change' command."

        info = data.split(" ")[2:]
        record = Record(name_, info)
        address_book.add_record(record)
        return f"{name_} with {info} was added"


def show_all():
    return address_book.data


@input_error
def info(data):
    name_ = data.strip().split(" ")[1]

    if name_ not in address_book.data:
        return f"{name_} doesn't have any information, call 'add' command to add {name_}"
    else:
        return address_book[name_]


@input_error
def delete(data):
    name_ = data.strip().split(" ")[1]

    if name_.lower() == "all":
        Record().delete_all()
        return "All information was deleted."
    elif name_ not in address_book.data:
        return f"{name_} doesn't have any information, you can't delete it"
    else:
        Record().delete(name_)
        return f"{name_} was deleted"


@input_error
def change(data):
    name_ = data.split(" ")[1]

    if name_ not in address_book.data:
        return f"{name_} doesn't have any information "
    else:
        if len(data.split(" ")) < 3:
            return "Enter the name with its new values"
        else:
            info = data.split(" ")[2:]
            Record().change(name_, info)
            return f"{name_}'s information was changed to {info}"


COMMANDS = {"hello": say_hello,
            "add": add,
            "info": info,
            "change": change,
            "show all": show_all,
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
