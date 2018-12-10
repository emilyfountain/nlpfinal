import nltk
import re

def get_syllables(word):
    vowel_groups = re.findall(r"[AEIOUYaeiouy]+", word)
    syllable_number = len(vowel_groups)
    if (re.search(r"[^aeiou]+e$", word)):
        syllable_number -= 1
    return syllable_number


def longest_word_length(document):
    longest_word = ""
    for d in document:
        for s in d:
            for w in s:
                if len(w) > len(longest_word):
                    longest_word = w
    return len(longest_word)
