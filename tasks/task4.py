def parse_input(user_input: str) -> tuple[str, ...]:
    cmd, *args = user_input.split()
    cmd = cmd.lower()
    return cmd, *args


def add_contact(args: tuple[str, ...], contacts: dict[str, str]) -> bool:
    name, phone = args[0], args[1]
    if name in contacts:
        return False
    else:
        contacts[name] = phone
        return True


def change_contact(args: tuple[str, ...], contacts: dict[str, str]) -> bool:
    name, new_phone = args[0], args[1]
    if name in contacts:
        contacts[name] = new_phone
        return True
    else:
        return False


def show_phone(args: tuple[str, ...], contacts: dict[str, str]) -> str | None:
    name = args[0]
    if name in contacts:
        phone = contacts[name]
        return f"{name}: {phone}"
    else:
        return None


def show_all(contacts: dict[str, str]) -> str:
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


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
                contact_added = add_contact(args, contacts)
                print("Contact added." if contact_added else "Contact already exists.")
            elif command == "change":  # "change [name] [new phone number]"
                contact_updated = change_contact(args, contacts)
                print(
                    "Contact updated." if contact_updated else "Contact doesn't exist."
                )
            elif command == "phone":  # "phone [name]"
                contact_phone = show_phone(args, contacts)
                print(contact_phone or "Contact doesn't exist.")
            elif command == "all":
                all_contacts = show_all(contacts)
                print(all_contacts or "No contacts.")
            else:
                print("Invalid command.")
        except Exception:
            print("Invalid arguments.")


if __name__ == "__main__":
    main()
