import random, nltk, labels_annotation, loadcorpus, feature_collector
COMMON_WORDS = feature_collector.common_word_list()

#create labeled data (with reading level attached)
def label_document(document, filename):
    labeled_document = (document, labels_annotation.get_label(filename))
    return labeled_document


#create feature sets
def create_feature_sets(labeled_docs):
    featuresets = []
    for item in labeled_docs:
        featuresets.append((get_features(item[0]), item[1]))
        #featuresets.append((get_features_smog_ari(item[0]), item[1]))
    size = int(len(featuresets) * 0.1)
    #print(size)
    #print("documents in test set^")
    train_set, test_set = featuresets[size:], featuresets[:size]
    return train_set, test_set


#get features
#these are the features we use in our classifier.
def get_features(full_text):
    features = {
                'average sent length': feature_collector.average_sentence_length(full_text),
                # 'longest_word': feature_collector.longest_word(full_text),
                'number of unique words': feature_collector.find_unique_words(full_text),
                'number of unique words, systematized':
                feature_collector.unique_words_system(full_text),
                'avg sentence length, systematized': feature_collector.sentence_length_system(full_text),
                'syllables': feature_collector.rank_syllables(full_text),
                'uncommon words': feature_collector.find_uncommon_words_system(full_text, COMMON_WORDS),
                'syllables systematized': feature_collector.rank_syllables_systemized(full_text)
                }
    # print(features)
    return features


#get features
#these are the SMOG and ARI reading level analyzers. They perform significantly
#below our features, getting about 30% accuracy.
def get_features_smog_ari(full_text):
    features = {
                'smog': labels_annotation.run_smog(labels_annotation.text_excerpt(full_text)),
                'ari': labels_annotation.run_ari(full_text)
                }
    return features


def train_classifier(train_set):
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    return classifier


def evaluate_classifier(classifier, test_set):
    print(nltk.classify.accuracy(classifier, test_set))


def run_classifier(classifier, text_file):
    classified = classifier.classify(get_features(text_file))
