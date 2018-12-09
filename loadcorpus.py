
import nltk
import classify_text
import smog

class Corpus(object):

    def __init__(self, data_root):
        self.wordlists = nltk.corpus.PlaintextCorpusReader(data_root, '.*.txt')

    def documents(self):
        return self.wordlists.fileids()

    def tokenize_sentences(self, filename):
        sentences = nltk.tokenize.sent_tokenize(self.wordlists.raw(filename))
        return [nltk.tokenize.word_tokenize(sent) for sent in sentences]

    def longest_word(self, filename):
        sentences = self.tokenize_sentences(filename)
        longest_word = ""
        for s in sentences:
            for w in s:
                if len(w) > len(longest_word):
                    longest_word = w
        return longest_word

    def number_of_sentences(self):
        sentences = []
        for file in self.wordlists.fileids():
            sentences.extend(self.tokenize_sentences(file))
        return len(sentences)

    def number_of_sentences_file(self, filename):
        sentences = []
        sentences.extend(self.tokenize_sentences(filename))
        print(len(sentences))




if __name__ == '__main__':
    #below: just playing around with the corpus
    corpus = Corpus('/Users/emilyfountain/programs/nlpfinal/test_data')
    print(corpus.documents())
    print(corpus.tokenize_sentences('bookmark.txt'))
    print(corpus.longest_word('bookmark.txt'))
    print(corpus.number_of_sentences())
    corpus.number_of_sentences_file('whoCanHelpMe.txt')

    #below: runs classifier on one text file 'bookmark.txt'.
    #runs successfully although obviously doesn't do the work we actually
    #need it to yet.
    labeled_sentences = classify_text.label_sentences(corpus.tokenize_sentences('bookmark.txt'))
    print(labeled_sentences)
    train_set, test_set = classify_text.create_feature_sets(labeled_sentences)
    classifier = classify_text.train_classifier(train_set)
    classify_text.evaluate_classifier(classifier, test_set)

    print(smog.run_ari(corpus.tokenize_sentences('bookmark.txt')))
