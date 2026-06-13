#!/usr/bin/env python3
class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        growth_rate: float = 0.0
    ) -> None:
        self.name = name
        self.height = float(height)
        self.age_days = age_days
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f'{self.name}: {self.height:.1f}cm, {self.age_days} days old')

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)

    def age(self) -> None:
        self.age_days += 1


if __name__ == '__main__':
    print('=== Plant Factory Output ===')

    my_garden = [
        Plant('Rose', 25.0, 30),
        Plant('Oak', 200.0, 365),
        Plant('Cactus', 5.0, 90),
        Plant('Sunflower', 80.0, 45),
        Plant('Fern', 15.0, 120)
    ]

    for plant in my_garden:
        print('Created: ', end='')
        plant.show()
