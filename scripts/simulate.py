from simulation_tools import *
from sys import argv

try:
    filename = f"../master-resultant-files/{argv[1]}.txt"
    num_trials = int(argv[2])
    
except:
    print("\tRun this script with a filename and number of trials, e.g.\n" \
        "\t> py \"p_distribution.py\" results 1000")
    exit()


NUM_SUITS = 4
NUM_RANKS = 6
NUM_CARDS = NUM_SUITS * NUM_RANKS

draws = [[draw_cards(num_drawn) for i in range(num_trials)] for num_drawn in range(NUM_CARDS + 1)]
expected_pairs = expected(draws)
distribution = p_distribution(draws)
output(filename, draws, expected_pairs, distribution)