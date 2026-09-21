import sys
import typing


def take_args(args: list[str]) -> None:
    if len(args) == 1:
        print("Usage:  ft_ancient_text.py <file>\n")
        return
    else:
        print("=== Cyber Archives Recovery === ")
        name: str = args[1]
        print(f"Accessing file: '{name}'")
    try:
        fd: typing.IO[str] = open(name, "r")
        try:
            text = fd.read()
            print("---\n")
            print(f"{text}")
            print("\n---")
        finally:
            fd.close()
            print(f"File '{name}' closed.")
    except FileNotFoundError as e:
        print(f"Error opening file {name}: {e}")
    except PermissionError as e:
        print(f"Error opening file {name}: {e}")
    except Exception as e:
        print(f"{e}")


def main() -> None:
    take_args(sys.argv)


if __name__ == "__main__":
    main()
