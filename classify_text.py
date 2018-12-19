import random, nltk, labels_annotation, loadcorpus, feature_collector


#tag document with whatever we need
#or do it sentence by sentence...whichever!
def tag_document():
    asdfasdflkj


#create labeled data (with reading level attached)
#change the smog analyzer to get a different result >:^)
def label_document(document, filename):
    labeled_document = (document, labels_annotation.get_label(filename))
    return labeled_document


#create feature sets
#labeled_docs is currently a list of lists(sentences), each sentence labeled
def create_feature_sets(labeled_docs):
    featuresets = []
    for item in labeled_docs:
        featuresets.append((get_features(item[0]), item[1]))
    size = int(len(featuresets) * 0.1)
    #print(size)
    #print("documents in test set^")
    train_set, test_set = featuresets[size:], featuresets[:size]
    return train_set, test_set


def get_features(full_text):
    features = {
                'average sent length': feature_collector.average_sentence_length(full_text),
                # 'longest_word': feature_collector.longest_word(full_text),
                'number of unique words': feature_collector.find_unique_words(full_text),
                'number of unique words, systemized':
                feature_collector.unique_words_system(full_text),
                'avg sentence length, systemized': feature_collector.sentence_length_system(full_text),
                'syllables': feature_collector.rank_syllables(full_text)
                }
    # print(features)
    return features


def train_classifier(train_set):
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    return classifier


def evaluate_classifier(classifier, test_set):
    print(nltk.classify.accuracy(classifier, test_set))


def run_classifier(classifier, text_file):
    classified = classifier.classify(get_features(text_file))
