import nltk
import classify_text
import labels_annotation
import random

class Corpus(object):

    def __init__(self, data_root):
        self.wordlists = nltk.corpus.PlaintextCorpusReader(data_root, '.*.txt')


    def documents(self):
        return self.wordlists.fileids()


    def tokenize_sentences(self, filename):
        sentences = nltk.tokenize.sent_tokenize(self.wordlists.raw(filename))
        return [nltk.tokenize.word_tokenize(sent) for sent in sentences]


    def number_of_sentences_file(self, filename):
        sentences = []
        sentences.extend(self.tokenize_sentences(filename))
        print(len(sentences))


if __name__ == '__main__':
    #corpus = Corpus('/Users/juliacathcart/Documents/Git/Github/nlpfinal-master')

# !!!Enter your data root HERE!!!
    corpus = Corpus('/Users/emilyfountain/programs/nlpfinal/test_data')

    labeled_documents = []
    for filename in corpus.documents():
        next_document_labeled = classify_text.label_document(corpus.tokenize_sentences(filename), filename)
        #print(next_document_labeled[1])
        labeled_documents.append(next_document_labeled)
    random.shuffle(labeled_documents)

    train_set, test_set = classify_text.create_feature_sets(labeled_documents)
    classifier = classify_text.train_classifier(train_set)
    print("Accuracy:")
    classify_text.evaluate_classifier(classifier, test_set)

    #classifier.show_most_informative_features(30)
