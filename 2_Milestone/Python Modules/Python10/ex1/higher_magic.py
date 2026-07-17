from collections.abc import Callable
from typing import Any


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hurts {target} for {power} HP"


def spell_combiner(
        spell1: Callable[[str, int], str], spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    def combined(target: str, power: int) -> tuple[str, str]:
        result1 = spell1(target, power)
        result2 = spell2(target, power)
        return result1, result2
    return combined


def power_amplifier(
        base_spell: Callable[[str, int], str], multiplier: int
) -> Callable[[str, int], str]:
    def amplifier(target: str, power: int) -> Any:
        result = base_spell(target, power * multiplier)
        return result
    return amplifier


def conditional_caster(
        condition: Callable[[str, int], bool], spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    def conditional(target: str, power: int) -> Any:
        if condition(target, power):
            result = spell(target, power)
            return result
        else:
            return "Spell fizzled"
    return conditional


def spell_sequence(
        spells: list[Callable[[str, int], str]]
) -> Callable[[str, int], list[str]]:
    def spells_list(target: str, power: int) -> list[str]:
        result: list[str] = []
        for spell in spells:
            result.append(spell(target, power))
        return result
    return spells_list


def is_powerful(_: str, power: int) -> bool:
    return power >= 15


if __name__ == "__main__":
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    result_combined = combined("Dragon", 10)
    print(f"Combined spell result: {result_combined}")

    amplifier = power_amplifier(heal, 3)
    result_amplifier = amplifier("Dragon", 10)
    print("\nTesting power amplifier...")
    original = heal("Dragon", 10)
    print(f"Original: {original} \nAmplified: {result_amplifier}")

    print("\nTesting conditional caster...")
    caster = conditional_caster(is_powerful, fireball)
    result_caster = caster("Dragon", 10)
    print(f"Condition not met: {result_caster}")
    result_caster = caster("Dragon", 20)
    print(f"Condition met: {result_caster}")

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal])
    result_sequence = sequence("Dragon", 10)
    print(f"Spell sequence result: {result_sequence}")
