import sys
import typing


class NoFile(Exception):
    pass


def take_name(args: list[str]) -> str:
    if len(args) == 1:
        print("Usage: ft_stream_management.py <file>", file=sys.stderr)
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
            print(f"Data saved in file '{name}'")
        finally:
            fd.close()
    except OSError as e:
        print(
            f"[STDERR] Error opening file '{name}': "
            f"{e}", file=sys.stderr
            )


def main() -> None:
    try:
        name = take_name(sys.argv)
        text = read_file(name)
    except NoFile:
        return
    except OSError as e:
        print(
            f"[STDERR] Error opening file '{name}': {e}",
            file=sys.stderr
            )
        return
    new_text = transform_text(text)
    print("Transform data:")
    print("---")
    print(new_text, end="")
    print("---")
    print("Enter new file name (or empty):")
    sys.stdout.flush()
    new_name = sys.stdin.readline().rstrip("\n")
    if new_name == "":
        print("Not saving data.")
    else:
        print(f"Saving data '{new_name}'")
        write_file(new_name, new_text)


if __name__ == "__main__":
    main()
