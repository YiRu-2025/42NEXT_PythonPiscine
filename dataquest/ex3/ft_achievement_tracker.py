import random


def gen_player_achievements(player: str, achievements: list[str]) -> set[str]:
    medal_num = random.randint(0, len(achievements))
    medal_lst = random.sample(achievements, medal_num)
    return set(medal_lst)


def main() -> None:
    print("=== Achievement Tracker System ===")
    achievements = ['Crafting Genius', 'World Savior', 'Master Explorer',
                    'Collector Supreme', 'Untouchable', 'Boss Slayer',
                    'Unstoppable', 'Strategist', 'Speed Runner', 'Survivor',
                    'Treasure Hunter', 'Hidden Path Finder', 'First Steps',
                    'Sharp Mind']
    players_lst: dict[str, set] = {'Alice': set(), 'Bob': set(),
                                   'Charlie': set(), 'Dylan': set()}

    for player in players_lst:
        players_lst[player] = gen_player_achievements(player, achievements)
        print(f"Player {player}: {players_lst[player]}")

    all_achive = set.union(*players_lst.values())
    print(f"\nAll distinct achievements: {all_achive}")

    comm_achive = set.intersection(*players_lst.values())
    print(f"\nCommon achivements: {comm_achive}\n")

    for player, medals in players_lst.items():
        others = set.union(
            *(s for name, s in players_lst.items() if name != player)
        )
        print(f"Only {player} has: {medals.difference(others)}")

    print()
    for player in players_lst:
        print(f"{player} is missing: "
              f"{set(achievements).difference(players_lst[player])}")


if __name__ == "__main__":
    main()
