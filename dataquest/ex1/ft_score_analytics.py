import sys

def main() -> None:
    argv = sys.argv[1:]
    print("=== Player Score Analytics ===")
    scores = []
    player = 0
    for i in argv:
        try:
            scores.append(int(i))
            player += 1
        except Exception:
            print(f"Invalid parameter: '{i}'")
    if player == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    print(f"Scores processed: {scores}")
    print(f"Total players: {player}")
    print(f"Total score: {sum(i for i in scores)}")
    print(f"Average score: {sum(i for i in scores) / player}")
    print(f"High score: {max(scores)}")
    print(f"Low score:{min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")
    return

if __name__ == "__main__":
    main()
