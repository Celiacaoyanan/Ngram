#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Process the raw corpus
Example of one line in raw corpus: 12	ruby	Ruby is a multi-platform open-source, dynamic object-oriented interpreted language, created by Yukihiro Matsumoto (Matz) in 1995.
Example of one line in corpus after processed: Ruby is a multi-platform open-source dynamic object-oriented interpreted language created by Yukihiro Matsumoto Matz in 1995
"""

if __name__ == '__main__':

    def process_corpus(corpus_dir):
        f_processed_corpus = open('corpus.txt', 'w')  # corpus.txt is used to store the corpus that are processed
        f_raw_corpus = open(corpus_dir, 'r')
        f_oneline_raw_corpus = f_raw_corpus.readlines()
        for line in f_oneline_raw_corpus:
            for i in (',', '(', ')', '/', '.', ' ', ' ', ':', '[', ']', '`', '"', '"'):
                line = line.replace(i, ' ')  # replace all the punctuation mark with a space
            list = line.split()  # put every word of a line into a list
            for w in list[2:]:  # leave out the first two words(the line number and the key word)
                w = w.strip()
                f_processed_corpus.write(w)
                f_processed_corpus.write(" ")
            f_processed_corpus.write('\n')

    import optparse

    parser = optparse.OptionParser()
    parser.add_option("-d", dest="dict_dir", help="dict_dir")
    (options, args) = parser.parse_args()

    if options.dict_dir:
        process_corpus(options.dict_dir)

