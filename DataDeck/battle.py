from ex0 import CreatureFactory, AquaFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    try:
        base = factory.create_base()
        print(base.describe())
        print(base.attack())
        evol = factory.create_evolved()
        print(evol.describe())
        print(evol.attack())
        print()
    except Exception as e:
        print(f"Caught error: {e}")
        return


def test_battle(fac_a: CreatureFactory, fac_b: CreatureFactory) -> None:
    print("Testing battle")
    try:
        creature_a = fac_a.create_base()
        creature_b = fac_b.create_base()
        print(creature_a.describe())
        print("vs.")
        print(creature_b.describe())
        print("fight!")
        print(creature_a.attack())
        print(creature_b.attack())
    except Exception as e:
        print(f"Caught error: {e}")
        return


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    test_factory(flame_factory)
    test_factory(aqua_factory)
    test_battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
