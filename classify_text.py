import random
import nltk
import smog
import loadcorpus
import feature_collector

#tag document with whatever we need
#or do it sentence by sentence...whichever!
def tag_document():
    asdfasdflkj


#create labeled data (with reading level attached)
#currently uses my "basic index" (A, B, C, D), from easy to hard
def label_document(document):
    labeled_document = (document, smog.get_basic_index(document))
    return labeled_document


#create feature sets
#labeled_docs is currently a list of lists(sentences), each sentence labeled
def create_feature_sets(labeled_docs):
    featuresets = []
    for item in labeled_docs:
        featuresets.append((get_features(item[0]), item[1]))
    size = int(len(featuresets) * 0.1)
    train_set, test_set = featuresets[size:], featuresets[:size]
    return train_set, test_set


#get features
def get_features(full_text):
    features = {'longest_word': full_text[-1][-1]}
    return features


#train classifier
def train_classifier(train_set):
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    return classifier


#evaluate classifier
def evaluate_classifier(classifier, test_set):
    print(nltk.classify.accuracy(classifier, test_set))


#run classifier
def run_classifier(classifier, text_file):
    classified = classifier.classify(basic_feature(text_file))
