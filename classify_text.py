
import random
import nltk

#tag document with whatever we need
#or do it sentence by sentence...whichever!
def tag_document():
    asdfasdflkj


#create labeled data
#this should iterate over ALL documents >:^)
#and give back a huge list of all the sentences...
#unless there's a better way to do it.
def label_sentences(tagged_documents):
    ###should have the given reading level below instead of the "0"
    labeled_sentences = [(sentence, 0) for sentence in tagged_documents]
    random.shuffle(labeled_sentences)
    return labeled_sentences

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
#i put sentence here but this could be anything (text file, etc)
#...and actually probably should be a text file, not a sentence
def run_classifier(classifier, sentence):
    classified = classifier.classify(basic_feature(sentence))


#if __name__ == '__main__':
    #labeled_data = create labeled data
