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
    standard_a: str = get_standard_str(a)
    standard_b: str = get_standard_str(b)
    a_counts: Dict[str, int] = count_letters(standard_a)
    b_counts: Dict[str, int] = count_letters(standard_b)
    for key in a_counts:
        if a_counts[key] != b_counts[key]:
            return False
    return True


def count_letters(s: str) -> Dict[str, int]:
    counts: Dict[str, int] = defaultdict(int)
    for letter in s:
        counts[letter] += 1
    return counts


def get_standard_str(s: str) -> str:
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
    for letter in normalize('NFD', s.lower()):
        if letter not in remove_set and not combining(letter):
            standard_str.append(letter)
    return ''.join(standard_str)
