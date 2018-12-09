import nltk
import re

def get_syllables(word):
    vowel_groups = re.findall(r"[AEIOUYaeiouy]+", word)
    print(vowel_groups)
    syllable_number = len(vowel_groups)
    if (re.search(r"[^aeiou]+e$", word)):
        syllable_number -= 1
    return syllable_number


if __name__ == "__main__":
    print(get_syllables("impotent"))
    print(get_syllables("impoutent"))
    print(get_syllables("irrigation"))
    print(get_syllables("irrigatione"))
