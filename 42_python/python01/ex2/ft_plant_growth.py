#!/usr/bin/env python3
class Plant:
    name: str = ''
    height: float = 0.0
    age_days: int = 0
    growth_rate: float = 0.0

    def show(self) -> None:
        print(f'{self.name}: {self.height:.1f}cm, {self.age_days} days old')

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)

    def age(self) -> None:
        self.age_days += 1


if __name__ == '__main__':
    print('=== Garden Plant Growth ===')

    rose = Plant()
    rose.name = 'Rose'
    rose.height = 25.0
    rose.age_days = 30
    rose.growth_rate = 0.8
    rose.show()

    initial_height = rose.height
    for day in range(1, 8):
        print(f'=== Day {day} ===')
        rose.grow()
        rose.age()
        rose.show()

    final_growth = round(rose.height - initial_height, 1)
    print(f'Growth this week: {final_growth}cm')
