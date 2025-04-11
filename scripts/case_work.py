from math import comb, factorial, prod
from collections import Counter
ks = 0
with open("../inputs.txt", 'r') as f:
    input = f.readline
    n, k, x = map(int, input().split())
    result = 0
    for i in range(n):
        line = input()
        case = list(map(lambda token: int(token[1:]), line.strip()[1:-1].split()))
        
        counts = Counter(case)
        repeats = prod(factorial(count) for count in counts.values())
        result += (comb(6, len(case)) 
                   * factorial(len(case)) / repeats 
                   * prod(comb(4, of_a_kind) ** count for of_a_kind, count in counts.items()))
        ks += sum(case)

        print(len(case), repeats, case)
        print(counts.items(), '\n')

print(f"Re-check cases: {k != ks / n}")
print(f"P_{k}(X = {x}) = {result/comb(24, k)}")
print(result)