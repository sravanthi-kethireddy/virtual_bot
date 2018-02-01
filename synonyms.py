from Lemmatizer import *
from nltk.corpus import wordnet as wn
#
# synonyms = []
#
# for syn in wn.synsets("good"):
#     for l in syn.lemmas():
#         synonyms.append(l.name())
#
#
# for i,j in enumerate(wn.synsets('water')):
#   print ((j.lemma_names))
# from nltk.corpus import wordnet as wn
# sent = "Obama met Putin the previous week"
#
# for i in query.split():
#     possible_senses = wn.synsets(i)
#     if possible_senses:
#         for j in range(4):
#             try:
#                 print (i, possible_senses[j].lemma_names)
#             except IndexError:
#                 pass
#     else:
#         print (i)

import spacy
nlp = spacy.load('en')
doc = nlp(u'dog')

def most_similar(word):
     by_similarity = sorted(word.vocab, key=lambda w: word.similarity(w), reverse=True)
     return [w.orth_ for w in by_similarity[:10]]
print (most_similar(doc))