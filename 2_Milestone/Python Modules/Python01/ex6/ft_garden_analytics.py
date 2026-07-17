class Plant:
    class Stats:
        def __init__(self) -> None:
            self.grow_calls: int = 0
            self.age_calls: int = 0
            self.show_calls: int = 0

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = height
        self._age: int = age
        self.stats: Plant.Stats = self.Stats()

    def grow(self, cm: float) -> None:
        self._height += cm
        self.stats.grow_calls += 1

    def age(self) -> None:
        self._age += 1
        self.stats.age_calls += 1

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm,"
              f" {self._age} days old")
        self.stats.show_calls += 1

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


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


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = round(self._height / 2)

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter
        self._shade_calls: int = 0

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")
        print(f"{self._shade_calls} shade")

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of "
            f"{round(self._height, 1)}cm long and"
            f" {self.trunk_diameter}cm wide."
        )
        self._shade_calls += 1


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant._name}]")
    stats: Plant.Stats = plant.stats
    print(f"Stats: {stats.grow_calls} grow, {stats.age_calls} age,"
          f" {stats.show_calls} show")

    if isinstance(plant, Tree):
        print(f"{plant._shade_calls} shade")


def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print("Is 30 days more than a year? ->", Plant.is_older_than_a_year(30))
    print("Is 400 days more than a year? ->", Plant.is_older_than_a_year(400))
    print()

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_stats(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_stats(rose)
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)
    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)
    print()

    print("=== Anonymous")
    anon_plant = Plant.anonymous()
    anon_plant.show()
    display_stats(anon_plant)


if __name__ == "__main__":
    ft_garden_analytics()
