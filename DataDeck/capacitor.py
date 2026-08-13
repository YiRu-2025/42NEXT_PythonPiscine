from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    try:
        base = factory.create_base()
        print("base:")
        print(base.describe())
        print(base.attack())
        print(base.heal())

        evol = factory.create_evolved()
        print("evolved:")
        print(evol.describe())
        print(evol.attack())
        print(evol.heal())
    except Exception as e:
        print(f"Caught error: {e}")


def test_transform(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    try:
        base = factory.create_base()
        print("base:")
        print(base.describe())
        print(base.attack())
        print(base.transform())
        print(base.attack())
        print(base.revert())

        evol = factory.create_evolved()
        print("evolved:")
        print(evol.describe())
        print(evol.attack())
        print(evol.transform())
        print(evol.attack())
        print(evol.revert())
    except Exception as e:
        print(f"Caught error: {e}")


def main() -> None:
    heal_fac = HealingCreatureFactory()
    tran_fac = TransformCreatureFactory()

    test_healing(heal_fac)
    print()
    test_transform(tran_fac)


if __name__ == "__main__":
    main()
