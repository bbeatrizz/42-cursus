def artifact_sorter(
        artifacts: list[dict[str, str | int]]
) -> list[dict[str, str | int]]:
    return sorted(artifacts, key=lambda artifact: artifact["power"],
                  reverse=True)


def power_filter(
        mages: list[dict[str, int]], min_power: int
) -> list[dict[str, int]]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spells: f"* {spells} *", spells))


def mage_stats(mages: list[dict[str, int]]) -> dict[str, float]:
    powers: list[int] = list(map(lambda mage: mage["power"], mages))

    return {
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": round(sum(powers) / len(powers), 2)
    }


if __name__ == "__main__":
    print("\nTesting artifact sorter...")
    artifacts: list[dict[str, str | int]] = [
        {"name": "Fire Staff", "power": 92, "type": "fire"},
        {"name": "Crystal Orb", "power": 85, "type": "orb"}
    ]
    sorted_artifacts = artifact_sorter(artifacts)

    print(
        f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} "
        f"power) comes before {sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
    )
    print("\nTesting spell transformer...")
    spells = ["fireball", "heal", "shield"]
    transformed = spell_transformer(spells)
    print(*transformed)
