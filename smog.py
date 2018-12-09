import nltk

def run_smog():
    asdfasdflkj

def run_ari(full_text_tokenized):
    total_sentences = 0
    words_in_sentences = 0
    letters_in_words = 0
    for sent in full_text_tokenized:
        total_sentences += 1
        for word in sent:
            words_in_sentences += 1
            letters_in_words += (len(word))
    print(total_sentences)
    print(words_in_sentences)
    print(letters_in_words)
    average_words = words_in_sentences / total_sentences
    average_letters = letters_in_words / words_in_sentences
    print(average_words)
    print(average_letters)
    ar_index = (average_words * 4.71) + (average_letters * 0.5) - 21.43
    return ar_index
