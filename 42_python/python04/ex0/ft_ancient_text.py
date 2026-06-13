#!/usr/bin/env python3
import sys


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename: str = sys.argv[1]
    archive = None
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        archive = open(filename, 'r')
        content: str = archive.read()
        print("---")
        print(content, end="")
        print("---")
    except FileNotFoundError as e:
        print(f"Error opening file '{filename}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{filename}': {e}")
    except IsADirectoryError as e:
        print(f"Error opening file '{filename}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if archive is not None:
            archive.close()
            print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
