"""
File Name:      Lemmatizer.py
Date Created:   Jan 31, 2018
Authors:        Sravanthi
Description:    Lemmatising module
"""

import nltk, string
from nltk.stem.wordnet import WordNetLemmatizer

query = "cats! running ran, cactus cactuses, cacti! community@ communities pupil dolphins"
translator = str.maketrans('', '', string.punctuation)
query = query.translate(translator)


class Tokenizer(object):
    def __init__(self):
        self.tokenizer = nltk.tokenize.TreebankWordTokenizer()

    def split(self, query):
        tokens = self.tokenizer.tokenize(query)
        return tokens


class Lemmatizer(object):
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        pass

    def lemmatization(self, query_tokens):
        words = []
        for each in query_tokens:
            word = self.lemmatizer.lemmatize(each)
            words.append(word)
        return words


def main():
    return lemmatized_words


if __name__ == '__main__':
    tokens_instance = Tokenizer()
    lemmatizer = Lemmatizer()
    tokens = tokens_instance.split(query)
    lemmatized_words = lemmatizer.lemmatization(tokens)

# print (main())
