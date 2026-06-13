#!/usr/bin/env python3
class Plant:
    def __init__(self,
                 name: str,
                 height: float,
                 age_days: int,
                 growth_rate: float = 0.0) -> None:
        self._name = name
        self._height = float(height) if height >= 0 else 0.0
        self._age_days = age_days if age_days >= 0 else 0
        self._growth_rate = growth_rate

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(new_height)

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age_days = new_age

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age_days} days old")

    def grow(self) -> None:
        self._height = round(self._height + self._growth_rate, 1)

    def age(self) -> None:
        self._age_days += 1


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    rose.set_height(25.0)
    print("Height updated: 25cm")
    rose.set_age(30)
    print("Age updated: 30 days")
    rose.set_height(-5.0)
    rose.set_age(-10)
    print("Current state: ", end="")
    rose.show()
