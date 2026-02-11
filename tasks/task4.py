def parse_input(user_input: str) -> tuple[str, ...]:
    cmd, *args = user_input.split()
    cmd = cmd.lower()
    return cmd, *args


def add_contact(args: tuple[str, ...], contacts: dict[str, str]) -> None:
    name, phone = args[0], args[1]
    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = phone
        print("Contact added.")


def change_contact(args: tuple[str, ...], contacts: dict[str, str]) -> None:
    name, new_phone = args[0], args[1]
    if name in contacts:
        contacts[name] = new_phone
        print("Contact updated.")
    else:
        print("Contact doesn't exist.")


def show_phone(args: tuple[str, ...], contacts: dict[str, str]) -> None:
    name = args[0]
    if name in contacts:
        phone = contacts[name]
        print(f"{name}: {phone}")
    else:
        print("Contact doesn't exist.")


def show_all(contacts: dict[str, str]) -> None:
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts.")


def main() -> None:
    contacts: dict[str, str] = {}

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in {"exit", "close"}:
            print("Good bye!")
            break

        try:
            if command == "hello":
                print("How can I help you?")
            elif command == "add":  # "add [name] [phone number]"
                add_contact(args, contacts)
            elif command == "change":  # "change [name] [new phone number]"
                change_contact(args, contacts)
            elif command == "phone":  # "phone [name]"
                show_phone(args, contacts)
            elif command == "all":
                show_all(contacts)
            else:
                print("Invalid command.")
        except Exception:
            print("Invalid arguments.")


if __name__ == "__main__":
    main()
