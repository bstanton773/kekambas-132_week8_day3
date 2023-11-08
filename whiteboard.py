# Write a function that takes two arrays of strings as input, a1 and a2. The function should 
# return an array r that contains all of the strings in a1 that are substrings of strings in a2, 
# sorted in lexicographical order.

# Example 1:
a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# solution(a1,a2) -> returns ["arp", "live", "strong"]

# Example 2:
# a1 = ["tarp", "mice", "bull"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

def solution(a1, a2):
    output = set()
    for word in a1:
        if word in ' '.join(a2):
            output.add(word)
    return sorted(output)



def solution(a1, a2):
    output = set(filter(lambda word: [x for x in a2 if word in x], a1))
    return sorted(output)