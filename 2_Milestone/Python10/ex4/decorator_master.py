from collections.abc import Callable
from functools import wraps
import time
from typing import Any


def spell_timer(func: Callable[[], str]) -> Callable[[], str]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> str:
        start: float = time.time()
        print(f"Casting {func.__name__}...")
        c: str = func(*args, **kwargs)
        print(f"Spell completed in {round(time.time() - start, 3)} seconds")
        return f"{c}"
    return wrapper


@spell_timer
def fireball() -> str:
    time.sleep(0.101)
    return "Fireball cast!"


def power_validator(min_power: int) -> Callable[[Any], Any]:
    def decorator(func: Callable[..., Any]) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power: int = args[2]
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[[Any], Any]:
    def decorator(func: Callable[..., Any]) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            i = 1
            while i <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except ValueError:
                    if i < max_attempts:
                        print("Spell failed, retrying... "
                              f"(attempt {i}/{max_attempts})")
                    i += 1
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


@retry_spell(3)
def fail_spell() -> str:
    raise ValueError("Spell failed!")


@retry_spell(1)
def valid_spell() -> str:
    return "Waaaaaaagh spelled !"


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c == " " for c in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")
    check_time = fireball()
    print(f"Result: {check_time}")

    print("\nTesting retrying spell...")
    fail_retry = fail_spell()
    print(fail_retry)
    valid_retry = valid_spell()
    print(valid_retry)

    print("\nTesting MageGuild...")
    valid_name = MageGuild()
    print(valid_name.validate_mage_name("Fire"))
    print(valid_name.validate_mage_name("Fire2"))
    print(valid_name.cast_spell("Fire", 15))
    print(valid_name.cast_spell("Fire", 5))
