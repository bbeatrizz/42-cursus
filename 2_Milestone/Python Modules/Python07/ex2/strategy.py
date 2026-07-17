from abc import ABC, abstractmethod
from ex1.capability import TransformCapability, HealCapability


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError("Battle error, aborting tournament: "
                                       f"Invalid Creature '{creature._name}' "
                                       "for this normal strategy")
        print(creature.attack())

    def is_valid(self, creature) -> bool:
        _ = creature
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError("Battle error, aborting tournament: "
                                       f"Invalid Creature '{creature._name}' "
                                       "for this aggresive strategy")
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())

    def is_valid(self, creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError("Battle error, aborting tournament: "
                                       f"Invalid Creature '{creature._name}' "
                                       "for this defensive strategy")
        print(creature.attack())
        print(creature.heal(creature._name))

    def is_valid(self, creature) -> bool:
        return isinstance(creature, HealCapability)
