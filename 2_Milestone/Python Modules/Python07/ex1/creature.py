from .capability import HealCapability, TransformCapability
from ex0.creature import Creature


class Flameling(Creature):
    def __init__(self) -> None:
        self._name = "Flameling"
        self._ctype = "Fire"

    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        self._name = "Pyrodon"
        self._ctype = "Fire/Flying"

    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self) -> None:
        self._name = "Aquabub"
        self._ctype = "Water"

    def attack(self) -> str:
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    def __init__(self) -> None:
        self._name = "Torragon"
        self._ctype = "Water"

    def attack(self) -> str:
        return "Torragon uses Hydro Pump!"


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        self._name = "Sproutling"
        self._ctype = "Grass"

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self, target) -> str:
        return f"{target} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        self._name = "Bloomelle"
        self._ctype = "Grass/Fairy"

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self, target) -> str:
        return f"{target} heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self)
        TransformCapability.__init__(self)
        self._name = "Shiftling"
        self._ctype = "Normal"

    def attack(self) -> str:
        if self._transformed is False:
            return "Shiftling attacks normally."
        else:
            return "Shiftling performs a boosted strike!"

    def transform(self) -> str:
        self._transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self)
        TransformCapability.__init__(self)
        self._name = "Morphagon"
        self._ctype = "Normal/Dragon"

    def attack(self) -> str:
        if self._transformed is False:
            return "Morphagon attacks normally."
        else:
            return "Morphagon unleashes a devastating morph strike!"

    def transform(self) -> str:
        self._transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        return "Morphagon stabilizes its form."
