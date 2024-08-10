"""
An algorithm for extracting the keywords of text.
"""

import nltk
#use this to download the corpus for the first time
#I already have them so I will just import them
#nltk.download('stopwords')
#nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import punkt
from rake_nltk import Rake

# Create a Rake instance
r = Rake()

# Text from which keywords will be extracted
text = "RAKE (Rapid Automatic Keyword Extraction) is a keyword extraction algorithm that automatically identifies relevant keywords and phrases in a text document."

# Extract keywords from the text
r.extract_keywords_from_text(text)

# Get the ranked keywords
keywords = r.get_ranked_phrases_with_scores()

# Print the extracted keywords and their scores
for score, kw in keywords:
    print("Keyword:", kw, "Score:", score)


from yake import KeywordExtractor

# Create a KeywordExtractor instance
kw_extractor = KeywordExtractor()

# Text from which keywords will be extracted
text = "YAKE (Yet Another Keyword Extractor) is a Python library for extracting keywords from text."

# Extract keywords from the text
keywords = kw_extractor.extract_keywords(text)

# Print the extracted keywords and their scores
for kw in keywords:
    print("Keyword:", kw[0], "Score:", kw[1])

