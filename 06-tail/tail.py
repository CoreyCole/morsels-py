"""
This week I want you to make a function that takes a sequence (like a list, string, or tuple) and a number n and returns the last n elements from the given sequence, as a list.

For example:

>>> tail([1, 2, 3, 4, 5], 3)
[3, 4, 5]
>>> tail('hello', 2)
['l', 'o']
>>> tail('hello', 0)
[]

As a bonus, make your function return an empty list for negative values of n: ✔️

>>> tail('hello', -2)
[]
As a second bonus, make sure your function works with any iterable, not just sequences. ✔️ For example:

>>> squares = (n**2 for n in range(10))
>>> tail(squares, 3)
[49, 64, 81]

See if you can make your function relatively memory efficient (if you're looping over a very long iterable, don't store the entire thing in memory).
"""

from typing import List

# TODO: memory efficiency
def tail(iterable: List, n: int) -> List:
    """Return the last n items of given iterable."""
    if n <= 0:
        return []
    sequence = list(iterable)
    return sequence[-n:]
