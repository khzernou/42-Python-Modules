#!/usr/bin/env python3
import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")
    players: list[str] = [
        "Djay", "daryl", "Carol", "maggie", "Alysa",
        "Michonne", "enid", "judith", "Magna"]

    print(f"Initial list of players: {players}\n")

    all_cap: list[str] = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_cap}\n")

    orig_cap: list[str] = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {orig_cap}\n")

    scores: dict[str, int] = {
            name: random.randint(1, 1000) for name in all_cap}
    avg: float = sum(scores.values()) / len(scores)
    print(f"Score average is {round(avg, 2)}")

    high_scores: dict[str, int] = {k: v for k, v in scores.items() if v > avg}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
