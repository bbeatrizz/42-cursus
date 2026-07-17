class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")

    plant1 = Plant("Rose", 25.0, 30)
    plant2 = Plant("Oak", 200.0, 365)
    plant3 = Plant("Cactus", 5.0, 90)
    plant4 = Plant("Sunflower", 80.0, 45)
    plant5 = Plant("Fern", 15.0, 120)

    plant1.show()
    plant2.show()
    plant3.show()
    plant4.show()
    plant5.show()


if __name__ == "__main__":
    ft_plant_factory()
