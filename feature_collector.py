import nltk
import re
import operator

def common_word_list():
    PUNCTUATION = [",", ".", ":", ";", "!", "?"]
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    from nltk.corpus import brown
    brown_sentences = brown.sents(categories='fiction')
    brown_vocab = {}
    for sent in brown_sentences:
        for word in sent:
            if word.lower() not in PUNCTUATION:
                if (word.lower() not in brown_vocab):
                    brown_vocab[word.lower()] = 1
                else:
                    brown_vocab[word.lower()] += 1
    sorted_brown_words = sorted(brown_vocab.items(), key=operator.itemgetter(1))
    most_common = [x[0] for x in sorted_brown_words[-500:]]
    return most_common


def find_uncommon_words(document, most_common):
    PUNCTUATION = [",", ".", ":", ";", "!", "?"]
    total_words = 0
    uncommon_words = 0
    for sent in document:
        for word in sent:
            if (word not in PUNCTUATION):
                total_words += 1
                if (word not in most_common):
                    uncommon_words += 1
    #print(round(uncommon_words/total_words, 2))
    return round(uncommon_words / total_words, 2)


def find_uncommon_words_system(document, most_common):
    uw_score = find_uncommon_words(document, most_common)
    if uw_score < 0.70:
        return 1
    if uw_score < 0.75:
        return 2
    if uw_score < 0.80:
        return 3
    if uw_score < 0.85:
        return 4
    if uw_score < 0.90:
        return 5
    else:
        return 6


def find_unique_words(document):
    vocab = {}
    total_words = 0
    for sent in document:
        for word in sent:
            total_words += 1
            if (word not in vocab):
                vocab[word] = 1
    return round(len(vocab) / total_words, 2)


def unique_words_system(document):
    unique_word_score = find_unique_words(document)
    if (unique_word_score < 0.1):
        return 1
    elif (unique_word_score < 0.3):
        return 2
    elif (unique_word_score < 0.5):
        return 3
    else:
        return 4


def get_syllables(word):
    vowel_groups = re.findall(r"[AEIOUYaeiouy]+", word)
    syllable_number = len(vowel_groups)
    if (re.search(r"[^aeiou]+e$", word)):
        syllable_number -= 1
    return syllable_number


def rank_syllables(document):
    PUNCTUATION = [",", ".", ":", ";", "!", "?"]
    syllables = 0
    total_words = 0
    for sent in document:
        for word in sent:
            if word not in PUNCTUATION:
                total_words += 1
                syllables_word = get_syllables(word)
                if syllables_word <= 2:
                    syllables += 0
                elif syllables_word == 3:
                    syllables += 1
                elif syllables_word == 4:
                    syllables += 2
                elif syllables_word == 5:
                    syllables += 4
                else:
                    syllables += 5
    return round(syllables / total_words, 2)




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


def sentence_length_system(document):
    avg_length = average_sentence_length(document)
    if (avg_length < 5):
        return 1
    elif(avg_length < 10):
        return 2
    elif(avg_length < 15):
        return 3
    elif(avg_length < 20):
        return 4
    elif(avg_length < 25):
        return 5
    elif(avg_length < 30):
        return 6
    elif(avg_length < 35):
        return 7
    else:
        return 8


def longest_word(document):
    longest_word_len = 0
    for sent in document:
        for word in sent:
            if (longest_word_len < len(word)):
                longest_word_len = len(word)
    return(longest_word_len)
