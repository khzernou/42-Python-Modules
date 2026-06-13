import alchemy


def main() -> None:
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")

    print("Now show that not all functions can be reached")

    print("Testing the hidden create_earth:")
    try:
        print(alchemy.create_earth())
    except AttributeError as error:
        print(error)


if __name__ == "__main__":
    main()
