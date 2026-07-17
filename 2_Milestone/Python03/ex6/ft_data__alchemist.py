import random


def ft_data_alchemist() -> None:

    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
                        'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {players}")
    cap_players = [n.capitalize() for n in players]
    print(f"New list with all names capitalized: {cap_players}")
    only_cap = [n for n in players if n == n.capitalize()]
    print(f"New list of capitalized names only: {only_cap}")
    scores = {name: random.randint(0, 1000) for name in cap_players}
    print(f"\nScore dict: {scores}")
    average = sum(scores.values()) / len(scores)
    print(f"Score average is {average:.2f}")
    h_scores = {
        name: score
        for name, score in scores.items()
        if score > average
    }
    print(f"High scores: {h_scores}")


if __name__ == "__main__":
    ft_data_alchemist()
