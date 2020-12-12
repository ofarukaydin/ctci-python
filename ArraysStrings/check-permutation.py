from collections import Counter


def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = Counter()
    for c in str1:
        counter[c] += 1
    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True


def check_permutation_hashmap(string1, string2):
    def create_hash_map(string):
        hashmap = {}
        for char in string:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] += 1
        return hashmap

    return create_hash_map(string1) == create_hash_map(string2)
