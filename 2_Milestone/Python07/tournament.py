from ex0.creature_factory import CreatureFactory, FlameFactory, AquaFactory
from ex1.creature_factory import (HealingCreatureFactory,
                                  TransformCreatureFactory)
from ex2 import (
    BattleStrategy,
    NormalStrategy, AggressiveStrategy, DefensiveStrategy,
    InvalidStrategyError
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory_a, strategy_a = opponents[i]
            factory_b, strategy_b = opponents[j]
            creature_a = factory_a.create_base()
            creature_b = factory_b.create_base()
            print("\n* Battle *")
            print(creature_a.describe())
            print(" vs.")
            print(creature_b.describe())
            print(" now fight!")
            try:
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
            except InvalidStrategyError as e:
                print(e)
                return


if __name__ == "__main__":
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(FlameFactory(), NormalStrategy()),
           (HealingCreatureFactory(), DefensiveStrategy())])
    print("\nTournament 1 (error)")
    print("[(Flameling+Aggressive), (Healing+Defensive)]")
    battle([(FlameFactory(), AggressiveStrategy()),
           (HealingCreatureFactory(), DefensiveStrategy())])
    print("\nTournament 2 (multiple)")
    print("[(Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive)]")
    battle([(AquaFactory(), NormalStrategy()),
           (HealingCreatureFactory(), DefensiveStrategy()),
           (TransformCreatureFactory(), AggressiveStrategy())])
