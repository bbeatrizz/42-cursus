import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        data = input("Enter new coordinates as floats in format 'x,y,z': ")

        parts = data.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(parts[0].strip())
            y = float(parts[1].strip())
            z = float(parts[2].strip())

            return (x, y, z)

        except ValueError as e:
            print(f"Error on parameter: {e}")


def distance_to_center(coord: tuple[float, float, float]) -> float:
    x, y, z = coord
    return math.sqrt(x**2 + y**2 + z**2)


def distance(c1: tuple[float, float, float],
             c2: tuple[float, float, float]) -> float:
    return math.sqrt(
        (c2[0] - c1[0])**2 +
        (c2[1] - c1[1])**2 +
        (c2[2] - c1[2])**2
    )


def main() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    first = get_player_pos()

    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")

    dist_center = distance_to_center(first)
    print(f"Distance to center: {round(dist_center, 4)}")

    print("\nGet a second set of coordinates")
    second = get_player_pos()

    dist_between = distance(first, second)
    print(
        "Distance between the 2 sets of coordinates: "
        f"{round(dist_between, 4)}"
    )


if __name__ == "__main__":
    main()
