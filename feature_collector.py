import nltk
import re

def find_unique_words(document):
    vocab = {}
    total_words = 0
    for sent in document:
        for word in sent:
            total_words += 1
            if (word not in vocab):
                vocab[word] = 1
    return round(len(vocab) / total_words, 2)


def get_syllables(word):
    vowel_groups = re.findall(r"[AEIOUYaeiouy]+", word)
    syllable_number = len(vowel_groups)
    if (re.search(r"[^aeiou]+e$", word)):
        syllable_number -= 1
    return syllable_number


def average_sentence_length(document):
    PUNCTUATION = [",", ".", ":", ";", "!", "?"]
    total_sentences = 0
    words_in_sentences = 0
    for sent in document:
        total_sentences += 1
        for word in sent:
            if (word not in PUNCTUATION):
                words_in_sentences += 1
    #i got a divide by zero error: fixed it like this for now, but might be
    #indicative of a larger problem
    if (total_sentences == 0):
        total_sentences = 1
    average_words = words_in_sentences / total_sentences
    return round(average_words)


def longest_word(document):
    longest_word_len = 0
    for sent in document:
        for word in sent:
            if (longest_word_len < len(word)):
                longest_word_len = len(word)
    return(longest_word_len)
