def input_temperature(temp_str: str,) -> int:
    try:
        temp = int(temp_str)
    except ValueError as e:
        raise ValueError(f"{e}")

    if temp > 40:
        raise ValueError(f"{temp}ºC is too hot for plants (max 40ªC)")
    if temp < 0:
        raise ValueError(f"{temp}ºC is too cold for plants (min 0ªC)")

    return int(temp)


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print()
    tests = ["25", "abc", "100", "-50"]

    for t in tests:
        print(f"Input data is '{t}'")

        try:
            temp = input_temperature(t)
            print(f"Temperature is now {temp}ºC")
            print()
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
            print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
