class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")

    def grow(self) -> None:
        self.height += self.growth_rate

    def age_one_day(self) -> None:
        self.age += 1


def ft_plant_growth() -> None:
    print("=== Garden Plant Growth ===")

    plant = Plant("Rose", 25.0, 30, 0.8)

    initial_height = plant.height
    plant.show()

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.age_one_day()
        plant.show()

    total_growth = plant.height - initial_height

    print(f"Growth this week: {round(total_growth, 1)}cm")


if __name__ == "__main__":
    ft_plant_growth()
