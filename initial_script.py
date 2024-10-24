# TEST GITHUB PUSH
from textblob import TextBlob
import nltk
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

text = """
I love unicorns. I love my mom.

"""

blob = TextBlob(text)
blob.tags  # [('The', 'DT'), ('titular', 'JJ'),
#  ('threat', 'NN'), ('of', 'IN'), ...]

blob.noun_phrases  # WordList(['titular threat', 'blob',
#            'ultimate movie monster',
#            'amoeba-like mass', ...])

for sentence in blob.sentences:
    print(sentence.sentiment.polarity)
# 0.060
# -0.341