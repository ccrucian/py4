import sys
import typing


class NoFile(Exception):
    pass


def take_name(args: list[str]) -> str:
    if len(args) == 1:
        print("Usage: ft_archive_data.py <file>")
        raise NoFile
    else:
        print(
            "=== Cyber Archives Recovery & Preservation ===\n"
            f"Accessing file '{args[1]}'")
    return args[1]


def read_file(name: str) -> str:
    fd: typing.IO[str] = open(name, "r")
    try:
        text = fd.read()
        print("---\n")
        print(f"{text}")
        print("\n---")
        return text
    finally:
        fd.close()
        print(f"File '{name}' closed.\n")


def transform_text(text: str) -> str:
    lines = text.split("\n")
    new_text = ""
    i = 0
    for line in lines:
        if i == len(lines) - 1 and line == "":
            continue
        new_text += line + "#\n"
        i += 1
    return new_text


def write_file(name: str, text: str) -> None:
    try:
        fd: typing.IO[str] = open(name, "w")
        try:
            fd.write(text)
        finally:
            fd.close()
    except FileNotFoundError as e:
        print(f"Error opening file {name}: {e}")
    except PermissionError as e:
        print(f"Error opening file {name}: {e}")
    except Exception as e:
        print(f"{e}")


def main() -> None:
    try:
        name = take_name(sys.argv)
        text = read_file(name)
    except NoFile:
        return
    except OSError as e:
        print(
            f"Error opening file '{name}': {e}"
            )
        return
    new_text = transform_text(text)
    print("Transform data:")
    print("---")
    print(new_text, end="")
    print("---")
    new_name = input("Enter new file name (or empty): ")
    if new_name == "":
        print("Not saving data.")
    else:
        print(f"Saving data '{new_name}'")
        write_file(new_name, new_text)
        print(f"Data saved in file '{new_name}'")


if __name__ == "__main__":
    main()
