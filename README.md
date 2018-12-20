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
