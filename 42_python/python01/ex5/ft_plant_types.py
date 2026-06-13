#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float = 0.0) -> None:
        self._name = name
        self._height = float(height) if height >= 0 else 0.0
        self._age_days = age_days if age_days >= 0 else 0
        self._growth_rate = growth_rate

    def get_height(self) -> float: return self._height
    def get_age(self) -> int: return self._age_days

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


class Flower(Plant):
    def __init__(self, name: str, height: float, age_days: int,
                 color: str, growth_rate: float = 0.0) -> None:
        super().__init__(name, height, age_days, growth_rate)
        self.color = color
        self._has_bloomed = False

    def bloom(self) -> None: self._has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._has_bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age_days: int,
                 trunk_diameter: float, growth_rate: float = 0.0) -> None:
        super().__init__(name, height, age_days, growth_rate)
        self.trunk_diameter = float(trunk_diameter)

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height:.1f}cm long and "
            f"{self.trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age_days: int,
                 harvest_season: str, growth_rate: float = 0.0) -> None:
        super().__init__(name, height, age_days, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self) -> None: super().grow()

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == '__main__':
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", growth_rate=2.1)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
