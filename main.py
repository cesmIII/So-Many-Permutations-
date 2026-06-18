from random import sample
from math import factorial as fact

def permutations(s: str):
    # Brute force solution
    chars = []
    while len(set(chars)) != fact(len(s)):
        shuffled_list = sample(s, len(s))
        chars.append("".join(shuffled_list))
    return list(set(chars))


perm = "abc"
print(permutations(perm))