class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


def test_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()

    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print()

    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    errors = [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!")
    ]
    print()
    print("Testing catching all garden errors...")
    for err in errors:
        try:
            raise err
        except GardenError as e:
            print(f"Caught GardenError: {e}")
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_errors()
