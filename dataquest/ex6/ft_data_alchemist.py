from random import randint


def main() -> None:
    print("=== Game Data Alchemist ===\n")
    init_names = ['Alice', 'bob', 'Charlie', 'dylan',
                  'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {init_names}")
    cap_all = [x.capitalize() for x in init_names]
    cap_only = [x for x in init_names if x == x.capitalize()]
    print(f"New list with all names capitalized: {cap_all}")
    print(f"New list of capitalized names only: {cap_only}")
    print()
    score_dict = {name: randint(1, 1000) for name in cap_all}
    score_avg = sum(x for x in score_dict.values()) / len(score_dict)
    score_high = {name: randint(round(score_avg), 1000) for name in cap_all}
    print(f"Score dict: {score_dict}")
    print(f"Score average is {round(score_avg, 2)}")
    print(f"High scores: {score_high}")


if __name__ == "__main__":
    main()
