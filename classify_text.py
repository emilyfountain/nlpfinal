
import random
import nltk

# class Classify_Text(object):
#
#     def __init__(self):

#create labeled data
def label_sentences(tagged_document):
    ###should have the reading level below instead of the "0"
    labeled_sentences = [(sentence, 0) for sentence in tagged_document]
    random.shuffle(labeled_sentences)

#create feature sets
def create_feature_sets(labeled_sentences):
    featuresets = [(basic_feature(sent), level) for (sent, level) in labeled_sentences]
    size = int(len(featuresets) * 0.1)
    train_set, test_set = featuresets[size:], featuresets[:size]
    return train_set, test_set

#pull features
def basic_feature(sentence):
    return {'first_word': sentence[0]}

#train classifier
def train_classifier(train_set):
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    return classifier

#evaluate classifier
def evaluate_classifier(classifier, test_set):
    print(nltk.classify.accuracy(classifier, test_set))

#run classifier



if __name__ == '__main__':
