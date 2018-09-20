import re
from typing import Dict


def count_words(input: str) -> Dict[str, int]:
    counts = dict()
    no_punctuation = re.sub(r'[,.?!¿¡]', '', input)
    for word in no_punctuation.split():
        normalized_word = word.lower()
        if normalized_word not in counts:
            counts[normalized_word] = 1
        else:
            counts[normalized_word] = counts[normalized_word] + 1
    return counts
