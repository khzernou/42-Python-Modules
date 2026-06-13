#!/usr/bin/env python3
import sys


def main() -> None:
    print("=== Command Quest ===")
    try:
        program_name: str = sys.argv[0]
        print(f"Program name: {program_name}")
        args: list[str] = sys.argv[1:]

        if not args:
            print("No arguments provided!")
        else:
            print(f"Arguments received: {len(args)}")
            for idx, arg in enumerate(args, start=1):
                print(f"Argument {idx}: {arg}")
        print(f"Total arguments: {len(sys.argv)}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
