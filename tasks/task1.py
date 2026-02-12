from pathlib import Path

from tasks.utils import print_error


def total_salary(path: str | Path, *, encoding: str = "utf-8") -> tuple[float, float]:
    path = Path(path)
    salaries: list[float] = []

    try:
        with path.open(encoding=encoding) as file:
            for line_n, line in enumerate(file, start=1):
                try:
                    _, salary = line.strip().split(",")
                    salary = float(salary.strip())
                    salaries.append(salary)
                except ValueError as e:
                    error_msg = str(e)
                    clean_line = line.strip()

                    if "not enough values to unpack" in error_msg:
                        print_error(
                            f"Line {line_n}: Missing comma or salary -> '{clean_line}'"
                        )
                    elif "too many values to unpack" in error_msg:
                        print_error(f"Line {line_n}: Too many values -> '{clean_line}'")
                    elif "could not convert string to float" in error_msg:
                        print_error(f"Line {line_n}: Invalid salary -> '{clean_line}'")
                    else:
                        raise
    except FileNotFoundError:
        print_error(f"File '{path.name}' was not found")
    except IsADirectoryError:
        print_error(f"File is exected, not a directory: '{path.name}'")
    except UnicodeError as e:
        print_error(f"File '{path.name}' is not encoded as '{encoding}'")

    if not salaries:
        return 0, 0

    total = sum(salaries)
    return total, total / len(salaries)


if __name__ == "__main__":
    total, average = total_salary("data/salaries.txt")
    print(
        f"Загальна сума заробітної плати: {total}\nСередня заробітна плата: {average}"
    )
