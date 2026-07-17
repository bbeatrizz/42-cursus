import sys
print("=== Player Score Analytics ===")

args: list[str] = sys.argv[1:]
scores: list[int] = []

for arg in args:
    try:
        scores.append(int(arg))
    except ValueError:
        print(f"Invalid parameter: '{arg}'")

if len(scores) == 0:
    print(
        "No scores provided. Usage: python3 ft_score_analytics.py <score1>"
        "<score2> ... "
        )
else:
    print("Scores processed:", scores)
    print("Total players: ", len(scores))
    print("Total score: ", sum(scores))
    print("Average score: ", sum(scores) / len(scores))
    print("High score: ", max(scores))
    print("Low score: ", min(scores))
    print("Score range:", max(scores) - min(scores))
