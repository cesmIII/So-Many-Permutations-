from itertools import permutations

def perms(string: str):
    """After hours of trying different things I discovered that python has a function that already do what I want"""
    return list(set(["".join(p) for p in permutations(string)]))



perm = 'abcde'
print(perms(perm))