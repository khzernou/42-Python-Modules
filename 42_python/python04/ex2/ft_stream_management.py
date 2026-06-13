#!/usr/bin/env python3
import sys


def main() -> None:
    if len(sys.argv) < 2:
        sys.stderr.write(
            "[STDERR] Usage: python3 ft_stream_management.py <file>\n"
        )
        return

    filename: str = sys.argv[1]
    reader = None
    writer = None

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")
    try:
        reader = open(filename, 'r')
        content: str = reader.read()
        print("---")
        print(content, end="")
        print("---")
        reader.close()
        print(f"File '{filename}' closed.")
        reader = None

        print("Transform data:")
        print("---")
        lines: list[str] = content.splitlines()
        transformed: str = "\n".join([f"{line}#" for line in lines])
        if content.endswith("\n"):
            transformed += "\n"
        print(transformed, end="")
        print("---")

        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        save_name: str = sys.stdin.readline().strip()

        if not save_name:
            print("Not saving data.")
            return

        print(f"Saving data to '{save_name}'")
        try:
            writer = open(save_name, 'w')
            writer.write(transformed)
            print(f"Data saved in file '{save_name}'.")
        except PermissionError as e:
            sys.stderr.write(
                f"[STDERR] Error opening file '{save_name}': {e}\n"
            )
            print("Data not saved.")
        except Exception as e:
            sys.stderr.write(f"[STDERR] Unexpected error: {e}\n")
            print("Data not saved.")

    except FileNotFoundError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
    except PermissionError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
    except IsADirectoryError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
    except Exception as e:
        sys.stderr.write(f"[STDERR] Unexpected error: {e}\n")
    finally:
        if reader is not None:
            reader.close()
        if writer is not None:
            writer.close()


if __name__ == "__main__":
    main()
