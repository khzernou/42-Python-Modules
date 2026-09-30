def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """sort artifacts by power level descending using lambda"""
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """filter mages power meets the min threshold"""
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """wrap each spell name with asterisk decorations"""
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """return max, min, and average power for all mages"""
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    return {
        "max_power": max(mages, key=lambda mage: mage["power"])["power"],
        "min_power": min(mages, key=lambda mage: mage["power"])["power"],
        "avg_power": round(
            sum(map(lambda mage: mage["power"], mages)) / len(mages), 2),
    }


def main() -> None:
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "arcane"},
        {"name": "Fire Staff", "power": 92, "type": "fire"},
        {"name": "Shadow Blade", "power": 78, "type": "dark"},
    ]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    first = sorted_artifacts[0]
    second = sorted_artifacts[1]
    print(
        f"{first['name']} ({first['power']} power) comes before "
        f"{second['name']} ({second['power']} power)"
    )

    mages = [
        {"name": "Alex", "power": 95, "element": "fire"},
        {"name": "Jordan", "power": 60, "element": "water"},
        {"name": "Riley", "power": 80, "element": "earth"},
    ]

    powerful = power_filter(mages, 75)
    print(f"\nMages with power >= 75: {[m['name'] for m in powerful]}")

    stats = mage_stats(mages)
    print(f"Stats: max={stats['max_power']}, "
          f"min={stats['min_power']}, avg={stats['avg_power']}")

    print("\nTesting spell transformer...")
    spells = ["fireball", "heal", "shield"]
    print(" ".join(spell_transformer(spells)))


if __name__ == "__main__":
    main()
