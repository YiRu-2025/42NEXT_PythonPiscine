from ex2 import (BattleStrategy, NormalStrategy,
                 AggressiveStrategy, DefensiveStrategy)
from ex1 import (CreatureFactory,
                 HealingCreatureFactory, TransformCreatureFactory)
from ex0 import AquaFactory, FlameFactory


def battle(fac_list: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(fac_list)} opponents involved")
    while len(fac_list) > 1:
        try:
            op1 = fac_list.pop(0)
            c1 = op1[0].create_base()
            s1 = op1[1]
            for op2 in fac_list:
                c2 = op2[0].create_base()
                s2 = op2[1]

                print("\n* Battle *")
                print(c1.describe())
                print("vs.")
                print(c2.describe())
                print("now fight!")

                print(s1.act(c1))
                print(s2.act(c2))
        except Exception as e:
            print(e)
    return


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()
    healing = HealingCreatureFactory()
    tranform = TransformCreatureFactory()

    norm_strategy = NormalStrategy()
    aggr_strategy = AggressiveStrategy()
    dfen_strategy = DefensiveStrategy()

    tour0 = [(flame, norm_strategy), (healing, dfen_strategy)]
    tour1 = [(flame, aggr_strategy), (healing, dfen_strategy)]
    tour2 = [(aqua, norm_strategy),
             (healing, dfen_strategy),
             (tranform, aggr_strategy)]

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle(tour0)
    print()

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle(tour1)
    print()

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle(tour2)


if __name__ == "__main__":
    main()
