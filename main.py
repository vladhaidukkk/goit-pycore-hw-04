from pathlib import Path
from colorama import Fore


# Task 1:
def print_error(message: str) -> None:
    print(f"{Fore.RED}{message}{Fore.RESET}")


def total_salary(path: str | Path) -> tuple[float, float]:
    path = Path(path)
    if not path.exists():
        print_error(f"File with salaries not found: '{path.absolute()}'")
        return 0, 0

    salaries: list[int] = []

    with open(path, encoding="utf-8") as file:
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


if __name__ == "__main__":
    # Task 1:
    total, average = total_salary("salaries.txt")
    print(
        f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"
    )
