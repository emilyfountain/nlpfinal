
import nltk

class Corpus(object):

    def __init__(self, data_root):
        self.wordlists = nltk.corpus.PlaintextCorpusReader(data_root, '.*')

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
        count = 0
        sentences = []
        for file in self.wordlists.fileids():
            sentences.extend(self.tokenize_sentences(file))
        for sent in sentences:
            count += 1
        return count




if __name__ == '__main__':
    corpus = Corpus('/Users/emilyfountain/programs/nlpfinal/test_data')
    print(corpus.documents())
    print(corpus.tokenize_sentences('bookmark.txt'))
    print(corpus.longest_word('bookmark.txt'))
    print(corpus.number_of_sentences())
