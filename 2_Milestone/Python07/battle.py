from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing Factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def test_fight(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    base1 = factory1.create_base()
    base2 = factory2.create_base()

    print(base1.describe())
    print(" vs.")
    print(base2.describe())
    print(" fight!")
    print(base1.attack())
    print(base2.attack())


if __name__ == "__main__":
    flame = FlameFactory()
    aqua = AquaFactory()
    test_factory(flame)
    print()
    test_factory(aqua)
    print()
    test_fight(flame, aqua)
