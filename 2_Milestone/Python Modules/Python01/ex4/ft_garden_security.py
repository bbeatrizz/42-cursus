class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = height
        self._age: int = age

    def show(self, header: str | None = None) -> None:
        if header:
            print(
                f"{header}: {self._name}: "
                f"{round(self._height, 1)}cm, "
                f"{self._age} days old"
            )
        else:
            print(
                f"{self._name}: "
                f"{round(self._height, 1)}cm, "
                f"{self._age} days old"
            )

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age
            print(f"Age updated: {self._age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


def ft_garden_security() -> None:
    print("=== Garden Security System ===")

    plant = Plant("Rose", 15.0, 10)

    plant.show("Plant created")
    print()
    plant.set_height(25.0)
    plant.set_age(30)
    print()
    plant.set_height(-5.0)
    plant.set_age(-10)
    print()
    plant.show("Current state")


if __name__ == "__main__":
    ft_garden_security()
