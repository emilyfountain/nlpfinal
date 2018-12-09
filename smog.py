import nltk
import re
import math
from feature_collector import get_syllables


def run_smog(full_text_tokenized):
    PUNCTUATION = [",", ".", ":", ";", "!", "?"]
    sentences = 0
    syllables = 0
    for sent in full_text_tokenized:
        sentences += 1
        s = [get_syllables(word) for word in sent if get_syllables(word)>2]
        syllables += len(s)
    return 1.0430*(math.sqrt(syllables*(30.0/sentences)))


def run_ari(full_text_tokenized):
    PUNCTUATION = [",", ".", ":", ";", "!", "?"]
    total_sentences = 0
    words_in_sentences = 0
    letters_in_words = 0
    for sent in full_text_tokenized:
        total_sentences += 1
        for word in sent:
            if (word not in PUNCTUATION):
                words_in_sentences += 1
                letters_in_words += (len(word))
    average_words = words_in_sentences / total_sentences
    average_letters = letters_in_words / words_in_sentences
    ar_index = (average_letters * 4.71) + (average_words * 0.5) - 21.43
    return ar_index

def get_smog_ari_avg(full_text_tokenized):
    return round((run_ari(full_text_tokenized) + run_smog(full_text_tokenized)) / 2)
