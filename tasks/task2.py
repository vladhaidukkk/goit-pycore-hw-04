import json
from pathlib import Path

from tasks.utils import print_error


def get_cats_info(path: str | Path, *, encoding: str = "utf-8") -> list[dict]:
    path = Path(path)
    cats: list[dict] = []

    try:
        with path.open(encoding=encoding) as file:
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
    except FileNotFoundError:
        print_error(f"File '{path.name}' was not found")
    except IsADirectoryError:
        print_error(f"File is exected, not a directory: '{path.name}'")
    except UnicodeError as e:
        print_error(f"File '{path.name}' is not encoded as '{encoding}'")

    return cats


if __name__ == "__main__":
    cats_info = get_cats_info("data/cats.txt")
    print(json.dumps(cats_info, indent=2))
