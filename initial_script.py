# import necessary packages
from textblob import TextBlob
import nltk

# run the following 2 lines of code once before you set up project, then can comment out
# nltk.download('punkt_tab')
# nltk.download('averaged_perceptron_tagger_eng')

# placeholder to put your sample text that will be run through sentiment analysis
text = """
I hate my life and I want to kill.
"""

# Positive response: I love my mother and I am so happy.
# Negative response: I hate my life and I want to kill.

# create a TextBlob object using the TextBlob package
blob = TextBlob(text)

# iterate through each sentence in the TextBlob object and print out the 
# sentiment polarity score
for sentence in blob.sentences:
    print("Polarity score: ", sentence.sentiment.polarity)

