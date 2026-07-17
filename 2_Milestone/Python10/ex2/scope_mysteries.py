from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    power: int = initial_power

    def acumulator(power_added: int) -> int:
        nonlocal power
        power = power + power_added
        return power
    return acumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def factory(item: str) -> str:
        return f"{enchantment_type} {item}"
    return factory


def memory_vault() -> dict[str, Callable[..., Any]]:
    memories = {}

    def store(key: str, value: Any) -> dict[str, int]:
        memories[key] = value
        return memories

    def recall(key: str) -> Any:
        if key in memories:
            return memories[key]
        else:
            return "Memory not found"
    return {
        'store': store,
        'recall': recall
    }


if __name__ == "__main__":
    print("Testing mage counter...")
    counter1 = mage_counter()
    for i in range(1, 3):
        counter_a = counter1()
        print(f"counter_a call {i}: {counter_a}")

    counter2 = mage_counter()
    counter_b = counter2()
    print(f"counter_b call 1: {counter_b}")

    print("\nTesting spell accumulator...")
    acumulator = spell_accumulator(100)
    added_power = acumulator(20)
    print(f"Base 100, add 20: {added_power}")
    added_power = acumulator(30)
    print(f"Base 100, add 30: {added_power}")

    print("\nTesting enchantment factory...")
    factory1 = enchantment_factory("Flaming")
    new_element = factory1("Sword")
    print(new_element)
    factory2 = enchantment_factory("Frozen")
    new_element2 = factory2("Shield")
    print(new_element2)

    print("\nTesting memory vault...")
    memory = memory_vault()
    print("Store 'secret' = 42")
    memory['store']('secret', 42)
    result = memory['recall']('secret')
    print(f"Recall 'secret': {result}")
    result2 = memory['recall']('unknown')
    print(f"Recall 'unknown': {result2}")
