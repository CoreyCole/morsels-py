"""
When solving this week's exercise, don't look back at your previous answers and avoid searching on the Internet until you get to the bonus. I'd like to make sure you struggle on this one. See if you can think up at least a couple different ways to solve it.

I want you to write a function that accepts two strings and returns True if the two strings are anagrams of each other.

Your function should work like this:

>>> is_anagram("tea", "eat")
True
>>> is_anagram("tea", "treat")
False
>>> is_anagram("sinks", "skin")
False
>>> is_anagram("Listen", "silent")
True

Make sure your function works with mixed case.

Before you try to solve any bonuses, I recommend you try to find at least two ways to solve this problem.

Okay now to the bonuses...

For the first bonus, make sure your function ignores spaces ✔️:

>>> is_anagram("coins kept", "in pockets")
True
For the second bonus, make sure your function also ignores punctuation ✔️:

>>> is_anagram("a diet", "I'd eat")
True
If you solved this one really quickly, here's a more challenging third bonus for you: try allowing accented latin characters but ignoring the accent marks. ✔️

>>> is_anagram("cardiografía", "radiográfica")
True
"""

from collections import defaultdict
from unicodedata import normalize, combining
from typing import Dict, List


def is_anagram(a: str, b: str) -> bool:
    a_dict: Dict[str, int] = defaultdict(int)
    b_dict: Dict[str, int] = defaultdict(int)
    for letter in get_standard_str(a):
        a_dict[letter] += 1
    for letter in get_standard_str(b):
        b_dict[letter] += 1
    for key in a_dict:
        if a_dict[key] != b_dict[key]:
            return False
    return True


def get_standard_str(a: str) -> str:
    remove_set = (
        '!',
        '.',
        ',',
        ':',
        ';',
        '\'',
        '"',
        ' '
    )
    standard_str: List[str] = []
    for letter in normalize('NFD', a.lower()):
        if letter not in remove_set and not combining(letter):
            standard_str.append(letter)
    return ''.join(standard_str)
