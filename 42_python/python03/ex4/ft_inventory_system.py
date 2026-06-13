#!/usr/bin/env python3
import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if ":" not in arg or arg.count(":") != 1:
                print(f"Error - invalid parameter '{arg}'")
                continue

            item, val_str = arg.split(":")
            if item in inventory:
                print(f"Redundant item '{item}' - discarding")
                continue
            try:
                quantity = int(val_str)
                inventory[item] = quantity
            except ValueError as e:
                print(f"Quantity error for '{item}': {e}")

    print(f"Got inventory: {inventory}")
    if not inventory:
        return

    item_list: list[str] = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_qty: int = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_qty}")

    for item, qty in inventory.items():
        percentage = (qty / total_qty) * 100
        print(f"Item {item} represents {percentage:.1f}%")

    most_abundant = max(inventory, key=lambda k: inventory[k])
    least_abundant = min(inventory, key=lambda k: inventory[k])

    print(
        f"Item most abundant: {most_abundant} "
        f"with quantity {inventory[most_abundant]}")
    print(
        f"Item least abundant: {least_abundant} "
        f"with quantity {inventory[least_abundant]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
