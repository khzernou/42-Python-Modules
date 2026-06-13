#!/usr/bin/env python3
import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["Djay", "Alysa", "Fran", "Natalie"]
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "use"]
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(
    event_list: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        idx = random.randrange(len(event_list))
        event = event_list.pop(idx)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_gen = gen_event()
    for i in range(1000):
        name, action = next(event_gen)
        print(f"Event {i}: Player {name} did action {action}")

    ten_events: list[tuple[str, str]] = []
    for _ in range(10):
        ten_events.append(next(event_gen))
    print(f"Built list of 10 events: {ten_events}")
    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()
