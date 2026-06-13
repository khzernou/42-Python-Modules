#!/usr/bin/env python3
import random

ALL_AVAILABLE_ACHIEVEMENTS: list[str] = [
    "Moewer Supreme",
    "Raid Shadow Legend Ad",
    "Normy Norminette User",
    "Oomf Chan",
    "Big Brother",
    "Cat Collector",
    "Hunter Eyes",
    "Explorer",
    "Mending",
    "Boss lvl 99",
    "Silk Touch",
    "Phantom Sprayer",
    "Radiant Wannabe",
    "Speed Runner",
    "Treasure Hunter",
    "Shadow Walker",
    "Dragon Slayer",
    "Night Owl",
    "Caffein Addict",
    "Last Stand",
    "Sir Meowsalot"
]


def gen_player_achievements() -> set[str]:
    count: int = random.randint(6, 13)
    chosen: list[str] = random.sample(ALL_AVAILABLE_ACHIEVEMENTS, count)
    return set(chosen)


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    players: dict[str, set[str]] = {
        "Djay": gen_player_achievements(),
        "Michaela": gen_player_achievements(),
        "Alysa": gen_player_achievements(),
        "Francesca": gen_player_achievements(),
    }
    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")
    all_distinct: set[str] = set().union(*players.values())
    print(f"All distinct achievements: {all_distinct}\n")

    common_achievements: set[str] = players["Alysa"].intersection(
        players["Djay"], players["Francesca"], players["Michaela"])
    print(f"Common achievements: {common_achievements}\n")

    for name, achievements in players.items():
        others: set[str] = set().union(
            *(acc for n, acc in players.items() if n != name)
        )
        only_player: set[str] = achievements.difference(others)
        print(f"Only {name} has: {only_player}")
    print("")
    all_possible: set[str] = set(ALL_AVAILABLE_ACHIEVEMENTS)
    for name, achievements in players.items():
        missing: set[str] = all_possible.difference(achievements)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
