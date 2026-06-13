#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:
    prompt = "Enter new coordinates as floats in format 'x,y,z': "
    while True:
        try:
            parts: list[str] = input(prompt).strip().split(",")
            if len(parts) != 3:
                print("Invalid syntax")
                continue

            for part in parts:
                try:
                    float(part.strip())
                except ValueError:
                    invalid_val: str = part.strip()
                    print(
                        f"Error on parameter '{invalid_val}': "
                        f"could not convert string to float: '{invalid_val}'"
                    )
                    raise ValueError
            x: float = float(parts[0].strip())
            y: float = float(parts[1].strip())
            z: float = float(parts[2].strip())
            return (x, y, z)
        except ValueError:
            continue


def main() -> None:
    print("=== Game Coordinate System ===")

    print("\nGet a first set of coordinates")
    p1: tuple[float, float, float] = get_player_pos()

    print(f"Got a first tuple: {p1}")
    print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")

    dist_to_center: float = math.sqrt(p1[0] ** 2 + p1[1] ** 2 + p1[2] ** 2)
    print(f"Distance to center: {dist_to_center:.4f}")

    print("\nGet a second set of coordinates")
    p2: tuple[float, float, float] = get_player_pos()

    dist_between: float = math.sqrt(
        (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2)
    print(f"Distance between the 2 sets of coordinates: {dist_between:.4f}")


if __name__ == "__main__":
    main()
