from collections import Counter
from random import shuffle

NUM_SUITS = 4
NUM_RANKS = 6
NUM_CARDS = NUM_SUITS * NUM_RANKS
UNSHUFFLED_DECK = [i // 4 for i in range(NUM_CARDS)]

def draw_cards(num_drawn: int) -> list[int]:
    shuffled_deck = UNSHUFFLED_DECK[:]
    shuffle(shuffled_deck)
    return shuffled_deck[:num_drawn]

def num_pairs(drawn_cards: list[int]) -> int:
    total_pairs = 0
    rank_occurences = [0] * NUM_RANKS
    for card in drawn_cards:
        if rank_occurences[card] == 1:
            total_pairs += 1
        rank_occurences[card] = (rank_occurences[card] + 1) % 2
    return total_pairs


def expected(draws: list[list[list[int]]]) -> list[float]:
    num_trials = len(draws[0])
    expected_pairs = [.0] * (NUM_CARDS + 1)
    for num_drawn, draws_case in enumerate(draws):
        trials = (num_pairs(draw) for draw in draws_case)
        expected_pairs[num_drawn] = sum(trials) / num_trials
    return expected_pairs

def p_distribution(draws: list[list[list[int]]]) -> list[dict[int, float]]:
    num_trials = len(draws[0])
    distribution = [{} for _ in range (NUM_CARDS + 1)]
    for num_drawn, draws_case in enumerate(draws):
        trials = (num_pairs(draw) for draw in draws_case)
        for pairs in trials:
            if pairs not in distribution[num_drawn]:
                distribution[num_drawn][pairs] = 0
            distribution[num_drawn][pairs] += 1
        for pairs in distribution[num_drawn]:
            distribution[num_drawn][pairs] /= num_trials
    return distribution

def output(filename: str, 
           draws: list[list[list[int]]], 
           expected_pairs: list[float], 
           distribution: list[dict[int, float]]) -> None:
    num_trials = len(draws)
    pairs_output = ""
    points_output = ""
    with open(filename, 'w') as f:
        # frequency stuff
        # i implemented a counter in p_distribution too, but shhhh
        
        pairs_frequencies = [Counter(num_pairs(draw) for draw in draw_case) for draw_case in draws]
        f.write(f"{num_trials} trials run!\nFrequency Data:\n")
        for num_drawn, pairs_frequencies_count in enumerate(pairs_frequencies):
            f.write(f"\nk = {num_drawn} cards drawn:\n")
            pairs_data = ""
            frequency_data = ""
            for pairs in sorted(pairs_frequencies_count):
                f.write(f"\t{pairs}: {pairs_frequencies_count[pairs]}\n")
                pairs_data += f"\t{pairs}\n"
                frequency_data += f"\t{pairs_frequencies_count[pairs]}\n"
            f.write(f"Pairs Data:\n{pairs_data}Frequency Data:\n{frequency_data}")

        # expected stuff
        f.write("\n#####################################\n")
        f.write(f"\n<# cards drawn>: <expected # pairs>, <expected # points>\n")
        for num_drawn, expected_pairs_val in enumerate(expected_pairs):
            f.write(f"{num_drawn}: {expected_pairs_val:.6f}, {num_drawn - 2 * expected_pairs_val:.6f}\n")
            pairs_output += f"{expected_pairs_val:.6f}\n"
            points_output += f"{num_drawn - 2 * expected_pairs_val:.6f}\n"

        f.write("\nPairs Data\n")
        f.write(pairs_output)
        f.write("\nPoints Data\n")
        f.write(points_output)


        # p distr stuff
        f.write("\n#####################################\n")
        f.write("Probability distributions for each number of cards drawn:\n<# pairs>: <P(# pairs)>\n")
        for num_drawn, num_drawn_distribution in enumerate(distribution):
            pairs_output = ""
            p_output = ""
            f.write(f"\nDistribution for {num_drawn} cards drawn:\n")
            for pairs in sorted(num_drawn_distribution):
                f.write(f"\t{pairs}: {num_drawn_distribution[pairs]:.6f}\n")
                pairs_output += f"\t{pairs}\n"
                p_output += f"\t{num_drawn_distribution[pairs]:.6f}\n"
            f.write(f"\n\tPairs Data for {num_drawn} cards drawn:\n")
            f.write(pairs_output)
            f.write(f"\n\tP Data for {num_drawn} cards drawn:\n")
            f.write(p_output)
