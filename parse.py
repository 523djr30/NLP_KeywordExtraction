"""
This program is meant to provide all the necessary 
functionality to parse a word document that is formatted 
with Verbatim, a template that is macros-enabled for 
high-school and college Policy Debate.
"""

import docx.styles
import docx.styles.style
from easygui import fileopenbox as filedialog
import docx
import yake

# opens a file dialog for only one selected file
path = filedialog(default="*.docx",filetypes=["*.docx"])

doc = docx.Document(path)

paragraphs = doc.paragraphs

i = 0
# used to skip the citation in the document
skip_next = False
text_to_clean = ""

for para in paragraphs:
    if para.style.name == doc.styles['Heading 4'].name:
        skip_next = True
    if para.style.name == doc.styles['Normal'].name:
        for run in para.runs:
            if skip_next:
                skip_next = False
                continue
            else:
                text_to_clean = run.text + text_to_clean

"""
Using 4 different algorithms recommended on GeeksforGeeks.com 
I will test which algorithm is best at finding the right keywords for debate cards.
Then I will use a 5th algorithm I designed modifed from the YAKE
ranking system to prioritize certain results in a way more accurate to debate.
"""
# textrank - seems like a failed test. It does not account for root words/phrases 
# which means that many similar words take up the top 10
import spacy
import pytextrank
# load a spaCy model, depending on language, scale, etc.
text = text_to_clean
nlp = spacy.load("en_core_web_sm")

# add PyTextRank to the spaCy pipeline
nlp.add_pipe("textrank")
rank_doc = nlp(text)

# examine the top-ranked phrases in the document
for phrase in rank_doc._.phrases[:30]:
    print(phrase.text)
print("---------------NEXT---------------")

text = " ".join(str(phrase.text) for phrase in rank_doc._.phrases)
rank_doc2 = nlp(text)
for phrase in rank_doc2._.phrases[:30]:
    print(phrase.text)
print("---------------NEXT---------------")
# ranking

# report
