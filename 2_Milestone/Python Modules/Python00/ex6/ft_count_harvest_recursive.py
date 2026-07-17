def ft_count_harvest_recursive() -> None:
    total_days: int = int(input("Days until harvest: "))

    def helper(current_day: int) -> None:
        if current_day > total_days:
            print("Harvest time!")
        else:
            print(f"Day {current_day}")
            helper(current_day + 1)
    helper(1)
