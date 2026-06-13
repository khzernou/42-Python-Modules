#!/usr/bin/env python3


def secure_archive(
    filename: str,
    mode: str = "r",
    content: str = ""
) -> tuple[bool, str]:
    try:
        with open(filename, mode) as archive:
            if mode == "r":
                data: str = archive.read()
                return (True, data)
            elif mode == "w":
                archive.write(content)
                return (True, "Content successfully written to file")
            else:
                return (False, f"Invalid mode: {mode}")
    except Exception as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "r"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "r"))

    test_file: str = "ancient_fragment.txt"
    print("\nUsing 'secure_archive' to read from a regular file:")
    read_res: tuple[bool, str] = secure_archive(test_file, "r")
    print(read_res)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    if read_res[0]:
        write_res: tuple[bool, str] = secure_archive(
            "vault_backup.txt", "w", read_res[1]
        )
        print(write_res)


if __name__ == "__main__":
    main()
