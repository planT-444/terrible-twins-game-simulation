from sys import argv
from random import shuffle

NUM_SUITS = 4
NUM_RANKS = 6
NUM_CARDS = NUM_SUITS * NUM_RANKS

try:
    FILENAME = f"../expected-resultant-files/{argv[1]}.txt"
    NUM_TRIALS = int(argv[2])
    
except:
    print("\tRun this script with a filename and number of trials, e.g.\n" \
        "\t> py \"Terrible Twins Game Simulation.py\" results 1000")
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

expected_pairs = [.0] * (NUM_CARDS + 1)
for num_drawn in range(NUM_CARDS + 1):
    trials = (num_pairs(draw(num_drawn)) for i in range(NUM_TRIALS))
    expected_pairs[num_drawn] = sum(trials) / NUM_TRIALS

pairs_output = ""
points_output = ""
with open(FILENAME, 'w') as f:
    f.write(f"{NUM_TRIALS} trials run!\n<# cards drawn>: <expected # pairs>, <expected # points>\n")
    for num_drawn, expected_pairs_val in enumerate(expected_pairs):
        f.write(f"{num_drawn}: {expected_pairs_val:.6f}, {num_drawn - 2 * expected_pairs_val:.6f}\n")
        pairs_output += f"{expected_pairs_val:.6f}\n"
        points_output += f"{num_drawn - 2 * expected_pairs_val:.6f}\n"

    f.write("\nPairs Data\n")
    f.write(pairs_output)
    f.write("\nPoints Data\n")
    f.write(points_output)
    