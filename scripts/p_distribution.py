from sys import argv
from random import shuffle

NUM_SUITS = 4
NUM_RANKS = 6
NUM_CARDS = NUM_SUITS * NUM_RANKS

try:
    FILENAME = f"../probability-resultant-files/{argv[1]}.txt"
    NUM_TRIALS = int(argv[2])
    
except:
    print("\tRun this script with a filename and number of trials, e.g.\n" \
        "\t> py \"p_distribution.py\" results 1000")
    exit()

unshuffled_deck = [i // 4 for i in range(NUM_CARDS)]

def draw(num_drawn: int) -> list[int]:
    shuffled_deck = unshuffled_deck[:]
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

distribution = [{} for _ in range (NUM_CARDS + 1)]
for num_drawn in range(NUM_CARDS + 1):
    trials = (num_pairs(draw(num_drawn)) for i in range(NUM_TRIALS))
    for pairs in trials:
        if pairs not in distribution[num_drawn]:
            distribution[num_drawn][pairs] = 0
        distribution[num_drawn][pairs] += 1
    for pairs in distribution[num_drawn]:
        distribution[num_drawn][pairs] /= NUM_TRIALS
        

with open(FILENAME, 'w') as f:
    f.write("Probability distributions for each number of cards drawn:\n<# pairs>: <P(# pairs)>\n")
    for num_drawn, num_drawn_distribution in enumerate(distribution):
        pairs_output = ""
        p_output = ""
        f.write(f"\nDistribution for {num_drawn} cards drawn:\n")
        for pairs in sorted(num_drawn_distribution):
            f.write(f"\t{pairs}: {num_drawn_distribution[pairs]}\n")
            pairs_output += f"\t{pairs}\n"
            p_output += f"\t{num_drawn_distribution[pairs]}\n"
        f.write(f"\n\tPairs Data for {num_drawn} cards drawn:\n")
        f.write(pairs_output)
        f.write(f"\n\tP Data for {num_drawn} cards drawn:\n")
        f.write(p_output)

    