import typing, random


def gen_event(players: list[str], actions: list[str]) -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)

def consume_event(events: list[tuple[str, str]]) -> typing.Generator[tuple[str, str], None, None]:
    while events:
        del_event = random.choice(events)
        events.remove(del_event)
        yield del_event

def main() -> None:
    players = ['alice', 'bob', 'charlie', 'dylan']
    actions = ['eat', 'run', 'sleep', 'grab', 'move', 'climb', 'swim', 'release', 'use']
    event_gen = gen_event(players, actions)
    for i in range(1000):
        res = next(event_gen)
        print(f"Event {i}: Player {res[0]} did action {res[1]}")
    event_list = []
    for _ in range(10):
        event_list.append(next(event_gen))
    print(f"Built list of {len(event_list)} events: {event_list}")
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()