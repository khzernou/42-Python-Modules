#!/usr/bin/env python3
class Plant:
    class _Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, {self._show_calls} show")

    def __init__(self, name: str, height: float, age_days: int,
                 growth_rate: float = 0.0) -> None:
        self._name = name
        self._height = float(height) if height >= 0 else 0.0
        self._age_days = age_days if age_days >= 0 else 0
        self._growth_rate = growth_rate
        self._stats = self._Stats()

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(plantclass):
        return plantclass("Unknown plant", 0.0, 0)

    def get_name(self) -> str: return self._name
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
        self._stats._show_calls += 1
        print(f"{self._name}: {self._height:.1f}cm, {self._age_days} days old")

    def grow(self) -> None:
        self._stats._grow_calls += 1
        self._height = round(self._height + self._growth_rate, 1)

    def age(self) -> None:
        self._stats._age_calls += 1
        self._age_days += 1


class Flower(Plant):
    def __init__(self, name: str, height: float, age_days: int,
                 color: str, growth_rate: float = 0.0) -> None:
        super().__init__(name, height, age_days, growth_rate)
        self.color = color
        self._has_bloomed = False

    def bloom(self) -> None:
        self._has_bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        print(f"{self._name} is blooming beautifully!" if self._has_bloomed
              else f"{self._name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float, age_days: int,
                 color: str, growth_rate: float = 0.0) -> None:
        super().__init__(name, height, age_days, color, growth_rate)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


class Tree(Plant):
    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def display(self) -> None:
            super().display()
            print(f"{self._shade_calls} shade")

    def __init__(self, name: str, height: float, age_days: int,
                 trunk_diameter: float, growth_rate: float = 0.0) -> None:
        super().__init__(name, height, age_days, growth_rate)
        self.trunk_diameter = float(trunk_diameter)
        self._stats: 'Tree._TreeStats' = self._TreeStats()

    def produce_shade(self) -> None:
        self._stats._shade_calls += 1
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height:.1f}cm long and "
            f"{self.trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


def display_plant_stats(plant: Plant) -> None:
    print(f"[{'statistics for'} {plant.get_name()}]")
    plant._stats.display()


if __name__ == '__main__':
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days more than a year? -> "
          f"{Plant.is_older_than_a_year(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red", 8.0)
    rose.show()
    display_plant_stats(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_plant_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    display_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 30.0)
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    display_plant_stats(sunflower)

    print("\n=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    display_plant_stats(unknown)
