import random


def gen_player_achievements() -> set[str]:
    all_achievements = [
        'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
        'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
        'First Steps', 'Collector Supreme', 'Untouchable',
        'Sharp Mind', 'Boss Slayer', 'Hidden Path Finder'
    ]

    n = random. randint(5, 9)
    return set(random.sample(all_achievements, n))


def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===")
    print()

    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    for name, ach in players.items():
        print(f"Player {name}: {ach}")

    all_achievements: set[str] = set()
    for ach in players.values():
        all_achievements = all_achievements.union(ach)

    print("\nAll distinct achievements:", all_achievements)

    common = None
    for ach in players.values():
        if common is None:
            common = ach
        else:
            common = common.intersection(ach)

    print("\nCommon achievements:", common)

    print()
    for name, ach in players.items():
        others: set[str] = set()
        for other_name, other_ach in players.items():
            if name != other_name:
                others = others.union(other_ach)

        unique = ach.difference(others)
        print(f"Only {name} has:", unique)

    print()
    for name, ach in players.items():
        missing = all_achievements.difference(ach)
        print(f"{name} is missing:", missing)


if __name__ == "__main__":
    ft_achievement_tracker()
