def secure_archive(
        name: str, action: int, content: str = ""
        ) -> tuple[bool, str]:
    if action == 0:
        try:
            with open(name, "w") as file:
                file.write(content)
            return (
                True, "'Content successfully written to file'")
        except Exception as e:
            return (False, str(e))
    else:
        try:
            with open(name, "r") as file:
                text = file.read()
            return (True, text)
        except Exception as e:
            return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("file.txt", 1))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("jkk", 1))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("../ancient_file.txt", 1))
    print()

    print("Using 'secure_archive' to write prev content to a new file:")
    print(secure_archive("new.txt", 0, "ciaone belli"))


if __name__ == "__main__":
    main()
