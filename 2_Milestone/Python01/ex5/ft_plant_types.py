class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = height
        self._age: int = age

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm,"
              f" {self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.has_bloomed: bool = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.has_bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")

    def bloom(self) -> None:
        self.has_bloomed = True


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of "
            f"{round(self._height, 1)}cm long and"
            f" {self.trunk_diameter}cm wide."
        )


class Vegetable(Plant):
    def __init__(self,
                 name: str, height: float,
                 age: int, harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutricional value: {self.nutritional_value}")

    def grow(self, cm: float) -> None:
        self._height += cm
        self.nutritional_value += 1

    def age(self) -> None:
        self._age += 1
        self.nutritional_value += 1


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow(42)
    for _ in range(20):
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    ft_plant_types()
