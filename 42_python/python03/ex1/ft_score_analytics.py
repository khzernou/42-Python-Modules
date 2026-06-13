#!/usr/bin/env python3
import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) <= 1:
        print("No scores provided.")
        print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    valid_scores: list[int] = []

    for arg in sys.argv[1:]:
        try:
            score: int = int(arg)
            valid_scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if not valid_scores:
        print("No scores provided.")
        print("Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    try:
        total_players: int = len(valid_scores)
        total_score: int = sum(valid_scores)
        average_score: float = total_score / total_players
        high_score: int = max(valid_scores)
        low_score: int = min(valid_scores)
        score_range: int = high_score - low_score

        print(f"Scores processed: {valid_scores}")
        print(f"Total players: {total_players}")
        print(f"Total score: {total_score}")
        print(f"Average score: {average_score:.1f}")
        print(f"High score: {high_score}")
        print(f"Low score: {low_score}")
        print(f"Score range: {score_range}")
    except Exception as e:
        print(f"An error occurred while calculating analytics: {e}")


if __name__ == "__main__":
    main()
