from collections import UserDict


class Field:
    pass


class Name:
    def __init__(self, name):
        self.name = name


class Phone:
    def __init__(self, phone):
        self.phone = phone


class Record:
    name = ""
    phone = ""
    Name = Name(name)
    Phone = Phone(phone)

    def delete(self, value):
        address_book.data.pop(value)


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name] = record.phone
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
    name_ = data.strip().split(" ")[1]
    phone_ = data.strip().split(" ")[2]
    record = Record()
    record.name = name_
    record.phone = phone_

    if name_ in address_book.data:
        return f"{name_} already has a number, call change function"

    elif not phone_.isnumeric():
        return f"{phone_} isn't a right input,enter a numeric one"

    else:
        address_book.add_record(record)
        return f"User {name_} with {phone_} was added."


def show_all():
    return address_book.data


@input_error
def phone(data):
    name_ = data.strip().split(" ")[1]

    if name_ not in address_book.data:
        return f"{name_} doesn't have a number, call 'add' command to add this user"
    else:
        return address_book[name_]


@input_error
def delete(data):
    name_ = data.strip().split(" ")[1]

    if name_ not in address_book.data:
        return f"{name_} doesn't have a number, you can't delete it"
    else:
        Record().delete(name_)
        return f"User {name_} was deleted"


@input_error
def change(data):
    name_ = data.strip().split(" ")[1]
    phone_ = data.strip().split(" ")[2]
    record = Record()
    record.name = name_
    record.phone = phone_

    if name_ not in address_book.data:
        return f"{name_} doesn't have a number, call 'add' command to add this user"
    elif not phone_.isnumeric():
        return f"{phone_} isn't a right input,enter a numeric one"
    else:
        address_book.add_record(record)
        return f"{name_}'s phone number was changed to {phone_}"


COMMANDS = {"hello": say_hello,
            "add": add,
            "phone": phone,
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

        elif user_command.split(" ")[0].lower() not in ["change", "phone", "add", "exit", "close", "goodbye", "delete"]:
            print("No such a command")

        elif user_command.lower() in ["exit", "close", "goodbye"]:
            print("Goodbye")
            break
        else:
            print(handler(user_command.split(" ")[0].lower())(user_command))


if __name__ == "__main__":
    main()
