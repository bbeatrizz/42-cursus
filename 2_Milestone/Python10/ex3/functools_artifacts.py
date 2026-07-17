from collections.abc import Callable
from typing import Any
from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    op_dict: dict[str, Callable[[int, int], int]] = {"add": operator.add,
                                                     "multiply": operator.mul,
                                                     "max": max, "min": min}
    if not spells:
        return 0
    if operation not in op_dict:
        raise ValueError(f"Unknown operation: {operation}")
    func = op_dict[operation]
    return reduce(func, spells)


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} attack on {target} with power {power}"


def partial_enchanter(
        base_enchantment: Callable[..., Any]
) -> dict[str, Callable[..., Any]]:
    part_fire = partial(base_enchantment, power=50, element="Fire")
    part_water = partial(base_enchantment, power=50, element="Water")
    part_air = partial(base_enchantment, power=50, element="Air")
    enchantments: dict[str, Callable[..., Any]] = {
        "First version:": part_fire,
        "Second version:": part_water,
        "Third version:": part_air}
    return enchantments


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def base_case(spell: Any) -> str:
        return "Unknown spell type"

    @base_case.register(int)
    def _(spell: str) -> str:
        return f"Damage spell: {spell} damage"

    @base_case.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @base_case.register(list)
    def _(spell: str) -> str:
        return f"Multi-cast: {len(spell)} spells"
    return base_case


if __name__ == "__main__":
    plus = spell_reducer([50, 50], "add")
    product = spell_reducer([10, 20, 30, 40], "multiply")
    max_number = spell_reducer([3, 5, 2, 40], "max")

    print("\nTesting spell reducer...")
    print(f"Sum: {plus}")
    print(f"Product: {product}")
    print(f"Max: {max_number}")

    print("\nTesting partial enchanter...")
    enchant = partial_enchanter(base_enchantment)
    print(enchant["First version:"](target="Dragon"))
    print(enchant["Second version:"](target="Wizard"))
    print(enchant["Third version:"](target="Goblin"))

    print("\nTesting memoized fibonacci...")
    fib_0 = memoized_fibonacci(0)
    print(f"Fib(0): {fib_0}")
    fib_1 = memoized_fibonacci(1)
    print(f"Fib(0): {fib_1}")
    fib_10 = memoized_fibonacci(10)
    print(f"Fib(0): {fib_10}")
    fib_15 = memoized_fibonacci(15)
    print(f"Fib(0): {fib_15}")

    print("\nTesting spell dispatcher...")
    spell = spell_dispatcher()
    print(spell(42))
    print(spell("fireball"))
    print(spell(["fireball", 42, 4]))
    print(spell(42.4))
