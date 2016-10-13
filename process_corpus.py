#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

if __name__ == '__main__':

    def process_corpus(corpus_dir):
        f = open('corpus.txt', 'w')
        f1 = open('excerpts.tsv', 'r')
        f2 = f1.readlines()
        for line in f2:
            for i in (',', '(', ')', '/', '.', ' ', ' ', ':', '[', ']', '`', '"', '"'):
                line = line.replace(i, ' ')
            list = line.split()
            for w in list[2:]:
                w = w.strip()
                f.write(w)
                f.write(" ")
            f.write('\n')

    import optparse

    parser = optparse.OptionParser()
    parser.add_option("-d", dest="dict_dir", help="dict_dir")
    (options, args) = parser.parse_args()

    if options.dict_dir:
        process_corpus(options.dict_dir)

