from pathlib import Path
from rich import print
from rich.panel import Panel
from rich.pretty import Pretty


def print_error(message: str) -> None:
    print(f"[red]{message}[/red]")


# Task 1:
def total_salary(path: str | Path) -> tuple[float, float]:
    path = Path(path)
    if not path.exists():
        print_error(f"File with salaries not found: '{path.absolute()}'")
        return 0, 0

    salaries: list[float] = []

    with path.open(encoding="utf-8") as file:
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

    total = sum(salaries)
    return total, total / len(salaries)


# Task 2:
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
    # Task 1:
    total, average = total_salary("salaries.txt")
    print(
        Panel(
            f"Загальна сума заробітної плати: {total}\nСередня заробітна плата: {average}",
            title="Task 1",
            title_align="left",
            padding=1,
            highlight=True,
        )
    )

    # Task 2:
    cats_info = get_cats_info("cats.txt")
    print(
        Panel(
            Pretty(cats_info),
            title="Task 2",
            title_align="left",
            padding=1,
        )
    )
