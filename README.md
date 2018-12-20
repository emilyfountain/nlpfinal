# nlpfinal

The Cathtain Reading Level Analyzer (alpha)

loadcorpus.py is the driver.
Run our program by typing "python3 loadcorpus.py" in your terminal window after confirming that the data root in the main method of loadcorpus is correct. You will want the data root to point to where our corpus ("test_data") is stored on your computer.

Note that as of now, our tagger and our classifier take quite a few minutes to run--please bear with us during the wait.

Relevant methods:

loadcorpus.py
This is our driver. It loads the corpus and controls the creation of the classifier.

classify_text.py
This file holds all the methods for creating and working with the classifier.

feature_collector.py
This file holds all the methods which extract features for use in our featuresets.

labels_annotation.py
This file labels the data, and holds methods that calculate SMOG and ARI reading levels.

labels.py
This file holds the annotations for each file.

results from last run:
accuracy: 0.6521739130434783
Most Informative Features:
number of unique words, systemized = 3                   A : C      =     36.1 : 1.0
    syllables systemized = 2                   A : D      =     23.6 : 1.0
avg sentence length, systemized = 3                   A : D      =     15.5 : 1.0
               syllables = 0.05                A : D      =      8.8 : 1.0
     average sent length = 12                  A : C      =      8.7 : 1.0
     average sent length = 27                  D : C      =      6.5 : 1.0
    syllables systemized = 4                   D : B      =      6.0 : 1.0
  number of unique words = 0.17                E : C      =      5.1 : 1.0
    syllables systemized = 3                   C : A      =      5.0 : 1.0
avg sentence length, systemized = 4                   C : A      =      4.9 : 1.0
               syllables = 0.1                 D : B      =      4.9 : 1.0
               syllables = 0.09                D : B      =      4.5 : 1.0
  number of unique words = 0.07                C : D      =      4.4 : 1.0
     average sent length = 31                  D : C      =      4.2 : 1.0
               syllables = 0.03                A : B      =      3.7 : 1.0
     average sent length = 28                  E : C      =      3.6 : 1.0
    syllables systemized = 5                   D : C      =      3.5 : 1.0
     average sent length = 13                  A : D      =      3.5 : 1.0
     average sent length = 17                  B : D      =      3.5 : 1.0
  number of unique words = 0.11                C : D      =      3.3 : 1.0
avg sentence length, systemized = 6                   D : C      =      3.3 : 1.0
     average sent length = 25                  D : C      =      3.2 : 1.0
     average sent length = 22                  C : B      =      3.1 : 1.0
  number of unique words = 0.13                E : C      =      3.1 : 1.0
     average sent length = 16                  B : D      =      3.0 : 1.0
     average sent length = 29                  B : C      =      3.0 : 1.0
avg sentence length, systemized = 7                   D : B      =      2.9 : 1.0
               syllables = 0.06                B : D      =      2.8 : 1.0
     average sent length = 30                  C : B      =      2.8 : 1.0
               syllables = 0.12                D : C      =      2.6 : 1.0
