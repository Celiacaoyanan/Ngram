#!/usr/bin/env python
# encoding: utf-8

"""
Ngram : Input number N and N-1 words, and predict top 10 words that is most likely to appear after those N-1 words according to the probabilities
"""


class Ngram():
    def __init__(self, n):
        self.words = self.load_corpus()
        #self.unigram = self.make_unigram(self.words)
        self.ngram = self.make_ngram(self.words, n)  # N gram model
        self.n_1gram = self.make_ngram(self.words, n-1)  # (N-1) gram model
        return

    def load_corpus(self):  # transform the raw corpus to a list
        with open('corpus.txt', 'r') as f:
            f_lines = f.readlines()
        words = []
        for line in f_lines:
            list = line.split()
            words.extend(list)
        return words

    """def make_unigram(self, words):  # unigram model
        unigram = {}  # stores the count of every word
        for i, word in enumerate(words):
            if not unigram.has_key(word):
                unigram[word] = 1
            else:
                unigram[word] += 1
        return unigram
    """

    def make_ngram(self, words, n):  #ngram model
        ngram_words = {}  # store the count of every n-1 words
        for i, word in enumerate(words):
            if i == len(words)-n+1:
                break
            x = []  # store the n-1 words temporarily
            for j in range(0, n):
                x.append(words[i+j])
            x1 = ' '.join(x)  # transform the list to string and connect words by spaces
            if not ngram_words.has_key(x1):
                ngram_words[x1] = 1
            else:
                ngram_words[x1] += 1
        return ngram_words

    # the first (n-1) words make up word_y, the first (n-1) words and the nth word make up word_x
    # calculate the probability of the nth word appearing after the n words
    def probability(self, word_x, word_y):
        a1 = self.ngram
        b1 = self.n_1gram
        a_count = a1.get(word_x, 0)  # get the count of the appearance of combination of first (n-1) words and the nth word
        b_count = b1.get(word_y, 0)  # get the count of the appearance of first (n-1) words
        p = float(a_count)/b_count
        return p

    def find_top10_probability(self, given_words, n):
        words = self.words
        plist = {}
        x = given_words
        x1 = ' '.join(x)
        if self.n_1gram.has_key(x1)== False:  # if the string that is made up by the given (n-1) words doesnt exist in the model, then output the following words
            print "The given words {0} are not in corpus.".format(x)
        else:
            for word in words:
                y = x + [word]
                y1 = ' '.join(y)
                pp = self.probability(y1, x1)
                plist[word] = pp
            sorted_plist = sorted(plist.iteritems(), key=lambda d: d[1], reverse=True)  # sort plist and get the tuple sorted_plist
            flag = 0
            for i in sorted_plist:  # output the top 10 words with the maximum probabilities
                flag = flag+1
                if flag == 11:
                    break;
                print i


if __name__ == "__main__":
    N = input("Input n: ")
    Given_words = []
    for i in range(0, N-1):
        w = raw_input("Input a word: ")
        Given_words.append(w)
    print "Given words: ", Given_words
    ng = Ngram(N)
    ng.find_top10_probability(Given_words, N)





