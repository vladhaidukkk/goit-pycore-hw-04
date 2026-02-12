import sys
from pathlib import Path

from colorama import Fore, Style

from tasks.utils import print_error


def print_dir(
    dir_path: str | Path,
    *,
    depth: int = 0,
    prev_last_flags: list[bool] | None = None,
) -> None:
    """Print a directory tree structure.

    Recursively traverses a directory and prints its contents in a tree format.

    Args:
        dir_path: Path to the directory to print.
        depth: Internal, do not specify.
        prev_last_flags: Internal, do not specify.

    Raises:
        ValueError: If the path does not exist or is not a directory.
    """
    dir_path = Path(dir_path)
    prev_last_flags = prev_last_flags or []

    if not dir_path.exists():
        raise ValueError(f"'{dir_path.absolute()}' does not exist")
    if not dir_path.is_dir():
        raise ValueError(f"'{dir_path.absolute()}' is not a directory")

    dir_items = list(dir_path.iterdir())

    # Build padding from ancestor flags, excluding the current level
    dir_padding = "".join(
        "   " if last_flag else "│  " for last_flag in prev_last_flags[:-1]
    )

    if depth == 0:
        dir_symbol = ""
    else:
        dir_symbol = "└──" if prev_last_flags[-1] else "├──"

    dir_name = str(dir_path) if depth == 0 else dir_path.name
    dir_empty_mark = " (empty)" if len(dir_items) == 0 else ""
    print(
        f"{dir_padding}{dir_symbol}{Fore.BLUE}{Style.BRIGHT}{dir_name}/{Style.RESET_ALL}{dir_empty_mark}"
    )

    for item_n, item in enumerate(dir_items, start=1):
        is_last_item = item_n == len(dir_items)
        if item.is_dir():
            print_dir(
                item,
                depth=depth + 1,
                prev_last_flags=prev_last_flags + [is_last_item],
            )
        else:
            # Build padding from ancestor flags, including the current level
            file_padding = "".join(
                "   " if last_flag else "│  " for last_flag in prev_last_flags
            )
            file_symbol = "└──" if is_last_item else "├──"
            print(
                f"{file_padding}{file_symbol}{Fore.GREEN}{item.name}{Style.RESET_ALL}"
            )


def main() -> None:
    args = sys.argv[1:]
    if len(args) != 1:
        print_error(f"Expected exactly 1 argument (path to directory), got {len(args)}")
        sys.exit(1)

    try:
        print_dir(args[0])
    except ValueError as e:
        print_error(e)


if __name__ == "__main__":
    main()
