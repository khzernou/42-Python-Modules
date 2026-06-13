#!/usr/bin/env python3
import sys


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    file_name: str = sys.argv[1]
    reader = None
    writer = None

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")
    try:
        reader = open(file_name, 'r')
        content: str = reader.read()
        print("---")
        print(content, end="")
        print("---")
        reader.close()
        print(f"File '{file_name}' closed.")
        reader = None

        print("Transform data:")
        print("---")
        lines: list[str] = content.splitlines()
        changed_content: str = "\n".join([f"{line}#" for line in lines])
        if content.endswith("\n"):
            changed_content += "\n"
        print(changed_content, end="")
        print("---")

        save_name: str = input("Enter new file name (or empty): ").strip()
        if not save_name:
            print("Not saving data.")
            return

        print(f"Saving data to '{save_name}'")
        try:
            writer = open(save_name, 'w')
            writer.write(changed_content)
            print(f"Data saved in file '{save_name}'.")
        except PermissionError as e:
            print(f"Error opening file '{save_name}': {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    except FileNotFoundError as e:
        print(f"Error opening file '{file_name}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{file_name}': {e}")
    except IsADirectoryError as e:
        print(f"Error opening file '{file_name}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if reader is not None:
            reader.close()
        if writer is not None:
            writer.close()


if __name__ == "__main__":
    main()
