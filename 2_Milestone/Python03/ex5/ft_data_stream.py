import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["bob", "alice", "dylan", "charlie"]
    actions = ["run", "eat", "sleep", "grab", "move",
               "climb", "swim", "release"]

    while True:
        ply = random.choice(players)
        act = random.choice(actions)
        yield (ply, act)


def consume_event(
        events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while events:
        index = random.randrange(len(events))
        event = events.pop(index)
        yield event


def ft_data_stream() -> None:

    print("=== Game Data Stream Processor ===")

    gen = gen_event()
    for i in range(1000):
        player, action = next(gen)
        print(f"Event {i}: Player {player} did action {action}")

    events = []
    for i in range(10):
        event = next(gen)
        events.append(event)
    print(f"Built list of 10 events: {events}")

    for event in consume_event(events):
        player, action = event
        print(f"Got event from list: ({player}, '{action}')")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    ft_data_stream()
