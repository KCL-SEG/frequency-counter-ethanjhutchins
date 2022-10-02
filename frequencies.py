"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for i in range (len(items)):
        flag = False
        freqKeys = frequencies.keys()
        for j in freqKeys:
            if str(items[i]) == j:
                flag = True
        x = frequencies.setdefault(str(items[i]), 1)
        if (flag):
            frequencies.pop(str(items[i]))
            frequencies[str(items[i])] = x + 1

    return frequencies
