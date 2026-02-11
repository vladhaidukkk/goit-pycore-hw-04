from pathlib import Path

from rich import print

from tasks.utils import print_error


def get_cats_info(path: str | Path) -> list[dict]:
    path = Path(path)
    if not path.exists():
        print_error(f"File with cats not found: '{path.absolute()}'")
        return []

    cats: list[dict] = []

    with path.open(encoding="utf-8") as file:
        for line_n, line in enumerate(file, start=1):
            try:
                id, name, age = line.strip().split(",")
                cats.append({"id": id, "name": name, "age": int(age)})
            except ValueError as e:
                error_msg = str(e)
                clean_line = line.strip()

                if "not enough values to unpack" in error_msg:
                    print_error(
                        f"Line {line_n}: Missing comma(s) or value(s) -> '{clean_line}'"
                    )
                elif "too many values to unpack" in error_msg:
                    print_error(f"Line {line_n}: Too many values -> '{clean_line}'")
                elif "invalid literal for int" in error_msg:
                    print_error(f"Line {line_n}: Invalid age -> '{clean_line}'")
                else:
                    raise

    return cats


if __name__ == "__main__":
    cats_info = get_cats_info("data/cats.txt")
    print(cats_info)
