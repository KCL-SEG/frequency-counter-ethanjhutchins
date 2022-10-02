"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for i in range (len(items)):
        x = frequencies.setdefault(str(items[i]), 1)
        if x:
            freq = frequencies.get(str(items[i]))
            frequencies.pop(str(items[i]))
            frequencies[str(items[i])] = freq + 1

    return frequencies
