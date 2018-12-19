import nltk
import re
import math, random
import labels
from feature_collector import get_syllables

#takes fileid and returns the label
#fileid must be in the labeled and available!
def get_label(filename):
    filename = filename[10:]
    for i in labels.all_labels:
        if filename == i[0] :
            return i[1]
    #return label

#takes texts as list of sentences
#retuns the first 10 sentences, middle 10, and last 10
#or less if there is not 30 sentences
def text_excerpt(full_text_tokenized):
    if len(full_text_tokenized) <= 30:
        print("Full text:\n")
        print(' '.join(list(full_text_tokenized)[0]))
        return full_text_tokenized
    else:
        mid_range = random.randint(11, len(full_text_tokenized)-20)
        first_10 = full_text_tokenized[0:10]
        middle_10 = full_text_tokenized[mid_range:mid_range+10]
        last_10 = full_text_tokenized[-10:]
        #print formatting so it is easy to read string
        first_10_text = [' '.join(i) for i in first_10]
        middle_10_text= [' '.join(i) for i in middle_10]
        last_10_text = [' '.join(i) for i in last_10]
        print("First 10 sentences:\n" + ' '.join(first_10_text))
        print("\nMid 10 sentences:\n" + ' '.join(middle_10_text))
        print("\nLast 10 sentences:\n" + ' '.join(last_10_text))
        #return tokenized sentences for use in SMOG test
        return list(first_10 + middle_10 + last_10)

#run smog test on result from text_excerpt to get 30 
def run_smog(excerpt_length_30):
    PUNCTUATION = [",", ".", ":", ";", "!", "?"]
    sentences = 0
    syllables = 0
    for sent in excerpt_length_30:
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
    #i got a divide by zero error: fixed it like this for now, but might be
    #indicative of a larger problem
    if (words_in_sentences == 0 or total_sentences == 0):
        words_in_sentences += 1
        total_sentences += 1
    average_words = words_in_sentences / total_sentences
    average_letters = letters_in_words / words_in_sentences
    ar_index = (average_letters * 4.71) + (average_words * 0.5) - 21.43
    return ar_index


def get_smog_ari_avg(full_text_tokenized):
    return round((run_ari(full_text_tokenized) + run_smog(full_text_tokenized)) / 2.0)


def get_basic_index(full_text_tokenized):
    basic_index = "LEVEL_X"
    ari_smog_avg = get_smog_ari_avg(full_text_tokenized)
    if (ari_smog_avg > 0 and ari_smog_avg < 4):
        basic_index = "LEVEL_A"
    elif (ari_smog_avg < 7):
        basic_index = "LEVEL_B"
    elif (ari_smog_avg < 10):
        basic_index = "LEVEL_C"
    elif (ari_smog_avg < 12):
        basic_index = "LEVEL_D"
    elif (ari_smog_avg < 17):
        basic_index = "LEVEL_E"
    print(basic_index)
    return basic_index
