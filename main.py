from math import factorial as ftl
from math import prod
from collections import Counter as ctr

def no_repeat(string: str):
    """Function for non repeating permutations"""
    chars = []
    while len(set(chars)) != ftl(len(string)):
        for char in range(len(string)):
            if char == 0:
                swap_s = string[char + 1:] + string[char]
                chars.append(swap_s)
            elif char < len(string) - 1:
                swap_s = string[:char] + string[char + 1:] + string[char]
                chars.append(swap_s)
            else:
                chars.append(string[char] + string[:char])
        string = string[1:] + string[0]
    return list(set(chars))

def repeating(string: str):
    """Function for repeating permutations"""
    ltrs = dict(ctr(string)).values()
    perms = int(ftl(len(string)) / prod([ftl(i) for i in ltrs]))
    chars = []
    while len(set(chars)) != perms:
        for char in range(len(string)):
            if char == 0:
                swap_s = string[char + 1:] + string[char]
                chars.append(swap_s)
            elif char < len(string) - 1:
                swap_s = string[:char] + string[char + 1:] + string[char]
                chars.append(swap_s)
            else:
                chars.append(string[char] + string[:char])
        string = string[1:] + string[0]
    return list(set(chars))
    

def permutations(s: str):
    if len(set(s)) == len(s):
        return no_repeat(s)
    else:
        return repeating(s)


perm = 'aaabbb'
print(permutations(perm))